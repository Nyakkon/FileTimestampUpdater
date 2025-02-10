import sys
import os
import configparser
from configparser import ConfigParser
from Modules.date_modifier import FileTimestampUpdater
from Modules.edit_date import open_gui

lang_path = os.path.join(os.getcwd(), "language.ini")
if not os.path.exists(lang_path):
    raise FileNotFoundError(f"Language configuration file not found: {lang_path}")
config = configparser.ConfigParser()
config.read(lang_path)
default_language = config.get("language", "default", fallback="en")
lang_folder = os.path.join(os.getcwd(), "lang", f"{default_language}.ini")
if not os.path.exists(lang_folder):
    raise FileNotFoundError(f"Language file not found: {lang_folder}")
config = ConfigParser()
config.read(lang_folder, encoding="utf-8")

def get_translation(key):
    """Lấy bản dịch từ file ngôn ngữ"""
    return config.get("ui", key, fallback=key)

def display_help():
    """Hiển thị hướng dẫn sử dụng"""
    print(f"\n{get_translation('help_title')}")
    print(f"{get_translation('help_option_1')}")
    print(f"{get_translation('help_option_1_detail')}")
    print(f"{get_translation('help_option_1_folder')}")
    print(f"\n{get_translation('help_option_2')}")
    print(f"{get_translation('help_option_2_detail')}")
    print(f"{get_translation('help_option_2_ui')}")
    print(f"\n{get_translation('help_option_3')}")
    print(f"{get_translation('help_option_3_detail')}")
    print(f"\n{get_translation('help_note')}")
    print("-" * 50)

def run():
    """Chương trình chính"""
    while True:
        print(f"\n{get_translation('menu_title')}")
        print(f"{get_translation('menu_option_1')}")
        print(f"{get_translation('menu_option_2')}")
        print(f"{get_translation('menu_option_3')}")
        print(f"{get_translation('menu_option_4')}")

        choice = input(f"{get_translation('your_choice')} (1/2/3/4): ").strip()

        if choice == "1":
            print(get_translation("menu_option_1"))
            updater = FileTimestampUpdater()
            updater.select_folder()
            print("\nPress Enter to return to the main menu.")
            input()

        elif choice == "2":
            print(get_translation("menu_option_2"))
            open_gui()

        elif choice == "3":
            display_help()
            print("\nPress Enter to return to the main menu.")
            input()

        elif choice == "4":
            print(get_translation("exit_message"))
            sys.exit()

        else:
            print(get_translation("invalid_choice"))

if __name__ == "__main__":
    run()
