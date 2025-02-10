import os
import time
from datetime import datetime
import pywintypes
import configparser
import win32file
import tkinter as tk
from tkinter import filedialog, messagebox
from tkcalendar import Calendar

# Đường dẫn thư mục gốc (chứa language.ini và thư mục lang)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Đường dẫn tới file `language.ini`
lang_path = os.path.join(base_dir, "language.ini")
if not os.path.exists(lang_path):
    raise FileNotFoundError(f"Không tìm thấy file cấu hình ngôn ngữ: {lang_path}")

# Đọc file `language.ini` với mã hóa UTF-8
config = configparser.ConfigParser()
with open(lang_path, 'r', encoding='utf-8') as f:
    config.read_file(f)

# Lấy ngôn ngữ mặc định hoặc đặt 'en' nếu không tồn tại
default_language = config.get('language', 'default', fallback='en')

# Đường dẫn tới file ngôn ngữ
lang_folder = os.path.join(base_dir, "lang")
lang_file_path = os.path.join(lang_folder, f"{default_language}.ini")
if not os.path.exists(lang_file_path):
    raise FileNotFoundError(f"Không tìm thấy file ngôn ngữ: {lang_file_path}")

# Đọc file ngôn ngữ với mã hóa UTF-8
lang_config = configparser.ConfigParser()
with open(lang_file_path, 'r', encoding='utf-8') as f:
    lang_config.read_file(f)

def get_translation(section, key, fallback=""):
    return lang_config.get(section, key, fallback=fallback)

# Lớp chính
class FileTimestampModifier:
    def __init__(self, project_dir=None):
        self.project_dir = project_dir or os.getcwd()
        self.log_directory = os.path.join(self.project_dir, "Logs")
        self.success_log_path = os.path.join(self.log_directory, "success.log")
        self.error_log_path = os.path.join(self.log_directory, "error.log")
        os.makedirs(self.log_directory, exist_ok=True)

    def log_message(self, message, log_type="success"):
        log_file = self.success_log_path if log_type == "success" else self.error_log_path
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"{datetime.now()} - {message}\n")

    def update_file_timestamps(self, directory, user_datetime):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                try:
                    new_timestamp = time.mktime(user_datetime.timetuple())
                    os.utime(file_path, (new_timestamp, new_timestamp))
                    file_handle = win32file.CreateFile(
                        file_path, win32file.GENERIC_WRITE,
                        win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE | win32file.FILE_SHARE_DELETE,
                        None, win32file.OPEN_EXISTING, 0, None
                    )
                    creation_time = pywintypes.Time(user_datetime)
                    win32file.SetFileTime(file_handle, creation_time, None, None)
                    file_handle.Close()
                    success_message = get_translation("ui", "success_message", fallback="Success: {filename} -> {timestamp}")
                    self.log_message(success_message.format(filename=filename, timestamp=user_datetime), log_type="success")
                except Exception as e:
                    error_message = get_translation("ui", "error_message", fallback="Error updating {filename}: {error}")
                    self.log_message(error_message.format(filename=filename, error=e), log_type="error")

    def process_timestamp_updates(self, folder, user_datetime):
        if folder:
            self.update_file_timestamps(folder, user_datetime)
            completion_message = get_translation("ui", "completion_message", fallback="Timestamps updated for files in {folder}.")
            messagebox.showinfo(get_translation("ui", "completion_title", fallback="Completed"),
                                completion_message.format(folder=folder))
        else:
            error_no_folder_message = get_translation("ui", "error_no_folder", fallback="No folder selected!")
            messagebox.showerror(get_translation("ui", "error_title", fallback="Error"),
                                 error_no_folder_message)

# Giao diện
def open_gui():
    def browse_folder():
        folder_path.set(filedialog.askdirectory())

    def apply_changes():
        try:
            date_selected = calendar.get_date()
            hour = int(hour_spinbox.get())
            minute = int(minute_spinbox.get())
            second = int(second_spinbox.get())

            year, month, day = map(int, date_selected.split("-"))
            user_datetime = datetime(year, month, day, hour, minute, second)

            if not folder_path.get():
                messagebox.showerror(get_translation("ui", "error_title", fallback="Error"),
                                     get_translation("ui", "error_no_folder", fallback="No folder selected!"))
                return

            modifier = FileTimestampModifier()
            modifier.process_timestamp_updates(folder_path.get(), user_datetime)
        except Exception as e:
            messagebox.showerror(get_translation("ui", "error_title", fallback="Error"),
                                 get_translation("ui", "error_generic", fallback="An error occurred: {error}").format(error=e))

    root = tk.Tk()
    root.title(get_translation("ui", "title", fallback="Update Timestamps"))
    root.geometry("300x450")

    tk.Label(root, text=get_translation("ui", "select_date", fallback="Select Date")).pack(pady=5)
    calendar = Calendar(root, date_pattern="yyyy-mm-dd")
    calendar.pack(pady=5)

    tk.Label(root, text=get_translation("ui", "select_hour", fallback="Select Time")).pack(pady=5)
    time_frame = tk.Frame(root)
    time_frame.pack(pady=5)

    tk.Label(time_frame, text=get_translation("ui", "hours", fallback="Hours")).grid(row=0, column=0)
    hour_spinbox = tk.Spinbox(time_frame, from_=0, to=23, width=5)
    hour_spinbox.grid(row=0, column=1)

    tk.Label(time_frame, text=get_translation("ui", "minutes", fallback="Minutes")).grid(row=0, column=2)
    minute_spinbox = tk.Spinbox(time_frame, from_=0, to=59, width=5)
    minute_spinbox.grid(row=0, column=3)

    tk.Label(time_frame, text=get_translation("ui", "seconds", fallback="Seconds")).grid(row=0, column=4)
    second_spinbox = tk.Spinbox(time_frame, from_=0, to=59, width=5)
    second_spinbox.grid(row=0, column=5)

    tk.Label(root, text=get_translation("ui", "select_folder", fallback="Select Folder")).pack(pady=5)
    folder_path = tk.StringVar()
    tk.Entry(root, textvariable=folder_path, state="readonly").pack(pady=5)
    tk.Button(root, text=get_translation("ui", "browse_folder", fallback="Browse Folder"), command=browse_folder).pack(pady=5)

    tk.Button(root, text=get_translation("ui", "apply_changes", fallback="Apply Changes"), command=apply_changes).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    open_gui()
