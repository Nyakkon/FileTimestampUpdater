import os
import time
import re
import configparser
from datetime import datetime
import pywintypes
import win32file
from tkinter import filedialog, Tk

lang_path = os.path.join(os.getcwd(), "language.ini")
config = configparser.ConfigParser()
config.read(lang_path)

default_language = config.get("language", "default", fallback="en")
lang_folder = os.path.join(os.getcwd(), "config", "lang", f"{default_language}.ini")

lang_config = configparser.ConfigParser()
lang_config.read(lang_folder, encoding="utf-8")

def get_translation(key, fallback="", section="ui"):
    return lang_config.get(section, key, fallback=fallback)

class FileTimestampUpdater:
    def __init__(self):
        self.project_dir = os.getcwd()
        self.log_directory = os.path.join(self.project_dir, "Logs")
        self.success_log_path = os.path.join(self.log_directory, "success.log")
        self.error_log_path = os.path.join(self.log_directory, "error.log")
        os.makedirs(self.log_directory, exist_ok=True)

    def log_message(self, message_key, log_file, **kwargs):
        message_template = get_translation(message_key, fallback=message_key)
        message = message_template.format(**kwargs)
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"{datetime.now()} - {message}\n")

    def extract_datetime_from_filename(self, filename):
        try:
            base_name, _ = os.path.splitext(filename)
            patterns = [
                r".*?(\d{4})(\d{2})(\d{2})[_-](\d{2})(\d{2})(\d{2})",
                r".*?(\d{4})(\d{2})(\d{2})[_-](\d{2})(\d{2})",
                r".*?(\d{4})[_-](\d{2})[_-](\d{2})[_-](\d{2})[_-](\d{2})[_-](\d{2})",
                r".*?(\d{4})[_-](\d{2})[_-](\d{2})[_-](\d{2})[_-](\d{2})",
            ]
            for pattern in patterns:
                match = re.search(pattern, base_name)
                if match:
                    if len(match.groups()) == 6:
                        year, month, day, hour, minute, second = map(int, match.groups())
                    elif len(match.groups()) == 5: 
                        year, month, day, hour, minute = map(int, match.groups())
                        second = 0
                    return datetime(year, month, day, hour, minute, second)
        except Exception as e:
            self.log_message("error_file", self.error_log_path, filename=filename, error=e)
        return None

    def update_file_timestamps(self, directory):
        print(get_translation("process_result"))
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                new_datetime = self.extract_datetime_from_filename(filename)
                if new_datetime:
                    new_timestamp = time.mktime(new_datetime.timetuple())
                    os.utime(file_path, (new_timestamp, new_timestamp))
                    try:
                        file_handle = win32file.CreateFile(
                            file_path, win32file.GENERIC_WRITE,
                            win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE | win32file.FILE_SHARE_DELETE,
                            None, win32file.OPEN_EXISTING, 0, None
                        )
                        creation_time = pywintypes.Time(new_datetime)
                        win32file.SetFileTime(file_handle, creation_time, None, None)
                        file_handle.Close()
                        self.log_message("success_update", self.success_log_path, filename=filename, datetime=new_datetime)
                        print(get_translation("success_print").format(filename=filename, datetime=new_datetime))
                    except Exception as e:
                        self.log_message("error_update", self.error_log_path, filename=filename, error=e)
                        print(get_translation("error_print").format(filename=filename, error=e))
                else:
                    self.log_message("invalid_file", self.error_log_path, filename=filename)
                    print(get_translation("invalid_print").format(filename=filename))

    def select_folder(self):
        root = Tk()
        root.withdraw() 
        root.attributes('-topmost', True) 
        folder_selected = filedialog.askdirectory(title=get_translation("folder_select", fallback="Select a folder to process"))
        if folder_selected:
            print(get_translation("folder_selected").format(folder=folder_selected))
            self.update_file_timestamps(folder_selected)
        else:
            print(get_translation("no_folder"))

if __name__ == "__main__":
    updater = FileTimestampUpdater()
    updater.select_folder()
