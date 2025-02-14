import sys
import os
from configparser import ConfigParser
from Modules.date_modifier import FileTimestampUpdater
from Modules.edit_date import open_gui


def load_language_config():
    lang_path = os.path.join(os.getcwd(), "language.ini")
    if not os.path.exists(lang_path):
        raise FileNotFoundError(f"Language configuration file not found: {lang_path}")

    config = ConfigParser()
    config.read(lang_path)
    default_language = config.get("language", "default", fallback="en")

    lang_file = os.path.join(os.getcwd(), "lang", f"{default_language}.ini")
    if not os.path.exists(lang_file):
        raise FileNotFoundError(f"Language file not found: {lang_file}")

    config.read(lang_file, encoding="utf-8")
    return config


def get_translation(config, key):
    return config.get("ui", key, fallback=key)


def display_help(config):
    print(f"\n{get_translation(config, 'help_title')}")
    print(f"{get_translation(config, 'help_option_1')}")
    print(f"{get_translation(config, 'help_option_1_detail')}")
    print(f"{get_translation(config, 'help_option_1_folder')}")
    print(f"\n{get_translation(config, 'help_option_2')}")
    print(f"{get_translation(config, 'help_option_2_detail')}")
    print(f"{get_translation(config, 'help_option_2_ui')}")
    print(f"\n{get_translation(config, 'help_option_3')}")
    print(f"{get_translation(config, 'help_option_3_detail')}")
    print(f"\n{get_translation(config, 'help_note')}")
    print("-" * 50)


def run():
    config = load_language_config()

    while True:
        print(f"\n{get_translation(config, 'menu_title')}")
        print(f"{get_translation(config, 'menu_option_1')}")
        print(f"{get_translation(config, 'menu_option_2')}")
        print(f"{get_translation(config, 'menu_option_3')}")
        print(f"{get_translation(config, 'menu_option_4')}")

        choice = input(f"{get_translation(config, 'your_choice')} (1/2/3/4): ").strip()

        if choice == "1":
            print(get_translation(config, "menu_option_1"))
            updater = FileTimestampUpdater()
            updater.select_folder()
            input(get_translation(config, "\n"+"enter_for_exit"))

        elif choice == "2":
            print(get_translation(config, "menu_option_2"))
            open_gui()

        elif choice == "3":
            display_help(config)
            input(get_translation(config, "\n"+"enter_for_exit"))

        elif choice == "4":
            print(get_translation(config, "exit_message"))
            sys.exit()

        else:
            print(get_translation(config, "invalid_choice"))


if __name__ == "__main__":
    run()
