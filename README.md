# 📌 File Timestamp Updater

🚀 **Version:** 1.0.1  
📧 **Contact:** [miko@wibu.me](mailto:miko@wibu.me)

---

## 📖 Overview
This script updates file timestamps based on their filenames, using specific date-time formats. It is particularly useful for organizing files by their creation or modification dates.

---

## 🛠 Installation and Setup
### 🔹 1. Install Python
Ensure Python is installed on your system. If not, download and install it from:
🔗 [Python Official Site](https://www.python.org/downloads/)

After installation, verify by running:
```sh
python --version
```
or
```sh
python3 --version
```

### 🔹 2. Install Required Dependencies
This script relies on the `pywintypes` and `win32file` libraries, which are part of `pywin32`. Install them using:
```sh
pip install -r requirements.txt
```
(Note: Ensure you have `requirements.txt` in the project directory with `pywin32` listed.)

### 🔹 3. Run the Script
Execute the script using:
```sh
python main.py
```

## 📂 Project Folder Structure
```text
/Project
    main.py            # Entry point of the application
    language.ini       # Configuration file for selecting language
    /Modules           # Contains core modules
        date_modifier.py    # Module to handle timestamp modification
        edit_date.py        # Module to extract and validate timestamps
    /lang
        en.ini         # English localization strings
        vi.ini         # Vietnamese localization strings
    /Logs
        success.log    # Logs of successfully processed files
        error.log      # Logs of files that encountered errors
```

---

### 🌐 How to Use Language Support

This project supports multiple languages for the user interface via the `language.ini` configuration file.

#### **Default Language Configuration**
The default language is specified in the `language.ini` file:
```ini
[default]
language = en
```
To change the language, edit the `language` field and specify the desired language code (e.g., `vi` for Vietnamese).

#### **Adding a New Language**
To add a new language:
1. Navigate to the `/lang` directory.
```text
/Project
    main.py            # Entry point of the application
    language.ini       # Configuration file for selecting language
    /lang
        en.ini         # English localization strings
        vi.ini         # Vietnamese localization strings
        other...       # Add your language
```
2. Create a new `.ini` file named after the language code (e.g., `es.ini` for Spanish).
```text
/Project
    main.py            # Entry point of the application
    language.ini       # Configuration file for selecting language
    /lang
        en.ini         # English localization strings
        vi.ini         # Vietnamese localization strings
        es.ini         # e.g., "es.ini" for Spanish
```

3. Add the translated key-value pairs. Example structure:
   ```ini
   [ui]
   help_title = Instrucciones de uso:
   help_option_1 = 1. Actualizar marcas de tiempo desde nombres de archivo:
   help_option_1_detail = - Seleccione la opción 1 si desea actualizar la fecha y la hora (creación y modificación) según el formato del nombre del archivo.
   help_option_2 = 2. Actualizar marcas de tiempo a través de la interfaz:
   help_option_2_detail = - Seleccione la opción 2 para ingresar manualmente las fechas y horas.
   ...
   ```

4. Update the `language.ini` file with the new language code:
   ```ini
   [default]
   language = es
   ```

#### **Switching Languages at Runtime**
The program automatically loads the selected language at runtime. If no language file is found, it defaults to English.

#### **Example of the Current Language Configuration**
Below is the default content of the English (`en.ini`) file:
```ini
[ui]
help_title = Usage Instructions:
help_option_1 = 1. Update timestamps from file names:
help_option_1_detail = - Select option 1 if you want to update the date and time (created and modified) based on the file name format (e.g., file_20230811_154500.txt).
help_option_1_folder = - You need to select the folder containing the files to process.
help_option_2 = 2. Update timestamps via the interface:
help_option_2_detail = - Select option 2 if you want to update the date and time by manually entering them through a graphical interface.
help_option_2_ui = - The interface will display a calendar and a clock for selecting the date and time.
help_option_3 = 3. Exit the program:
help_option_3_detail = - Select option 3 to exit the program.
help_note = Note: Successfully processed or failed files will be logged in the Logs folder.
menu_title = Select an option:
menu_option_1 = 1. Update timestamps from file names (file.extension)
menu_option_2 = 2. Update timestamps via the interface (select date and time)
menu_option_3 = 3. Usage instructions
menu_option_4 = 4. Exit the program
invalid_choice = Invalid choice. Please try again.
exit_message = Exiting the program. Goodbye!
title = Update Timestamps
select_date = Select Date:
select_hour = Select Time:
select_folder = Select Folder:
apply_changes = Apply
browse_folder = Browse Folder
completion_title = Completed
completion_message = Timestamps updated for files in {folder}.
error_title = Error
error_no_folder = No folder selected!
error_generic = An error occurred: {error}
success_message = Success: {filename} -> {timestamp}
error_message = Error updating {filename}: {error}
hours = Hours
minutes = Minutes
seconds = Seconds
error_file = Error {filename}: {error}
success_update = Success: {filename} -> {datetime}
error_update = Error updating Creation Date for {filename}: {error}
invalid_file = Invalid file: {filename}
success_print = [SUCCESS]: {filename} -> {datetime}
error_print = [ERROR]: Failed to update Creation Date for {filename}: {error}
invalid_print = [ERROR]: Invalid file: {filename}
folder_selected = Selected folder: {folder}
no_folder = No folder selected.
process_result = \n--- Processing Results ---
folder_select = Select a folder to process
```
With these steps, you can add or modify language configurations for your project.


---

## 📝 How It Works
### 📂 1. Select a Directory
- When the script runs, a file dialog will appear, allowing you to select a folder.
- It will process all files within the selected directory.

### 🕒 2. Extract Timestamp from Filename
The script recognizes several date-time patterns in filenames:
- `YYYYMMDD_HHMMSS` (e.g., `20250302_110320`)
- `YYYYMMDD_HHMM` (e.g., `20250302_1103`)
- `YYYY_MM_DD_HH_MM_SS` (e.g., `2025_03_02_11_03_20`)
- `YYYY_MM_DD_HH_MM` (e.g., `2025_03_02_11_03`)

The `edit_date.py` module plays a key role in:
- **Accurate Pattern Matching:** Validating and extracting timestamps.
- **Error Logging:** Handling invalid or malformed filenames gracefully.
- **Edge Case Management:** Skipping files with incomplete timestamps.

### ⏳ 3. Update File Timestamps
- The script modifies the **last modified time** and **creation time** of each file based on the extracted timestamp.
- Logs for both successes and errors are saved in `Logs/success.log` and `Logs/error.log`.

---

## 🔍 Detailed Report
### **Changelog**
**Version 1.0.1 Updates:**
- Enhanced `edit_date.py` for better timestamp validation and logging.
- Added support for multilingual interface (English and Vietnamese).
- Improved logging format to include more context, such as file paths and error descriptions.
- Refactored code for better efficiency and modularity.
- Updated GUI responsiveness and user feedback.

### **File Structure**
- **`main.py`**: Entry point of the script.
- **`Modules/`**: Contains core logic.
  - `date_modifier.py`: Handles timestamp modification.
  - `edit_date.py`: Extracts and validates timestamps from filenames.
- **`lang/`**: Localization files.
  - `en.ini`: English strings.
  - `vi.ini`: Vietnamese strings.
- **`language.ini`**: Configuration file for selecting the language.

### **Known Limitations**
- Only supports filenames with specific timestamp patterns.
- Requires Python to be installed on the system.

---

## ✅ Test Cases
### **Test Environment**
- OS: Windows 10
- Python Version: 3.10
- Dependencies: pywin32 (latest version)

### **Test Scenarios**
#### Test Case 1: Valid Timestamp in Filename
**Filename:** `photo_20250302_110320.jpg`  
**Expected Result:** Timestamps updated to 2025-03-02 11:03:20.  
**Actual Result:** ✅ Success

#### Test Case 2: Invalid Timestamp in Filename
**Filename:** `photo_invalid.jpg`  
**Expected Result:** File skipped with an error logged.  
**Actual Result:** ✅ Success, logged in `Logs/error.log`.

#### Test Case 3: Edge Case - Incomplete Timestamp
**Filename:** `photo_2025_03.jpg`  
**Expected Result:** File skipped due to invalid format.  
**Actual Result:** ✅ Success, logged in `Logs/error.log`.

#### Test Case 4: Multilingual Interface
**Configuration:** Set `language.ini` to `vi`.  
**Expected Result:** Vietnamese UI strings displayed.  
**Actual Result:** ✅ Success

#### Test Case 5: Directory with Mixed Files
**Directory Contents:**  
- `photo_20250302_110320.jpg` (valid)  
- `document_invalid.pdf` (invalid)  

**Expected Result:** Valid file processed; invalid file logged.  
**Actual Result:** ✅ Success with detailed logs.

---

## 📜 Logging
- **✅ Success Log (`Logs/success.log`)**: Contains details of successfully processed files.
- **❌ Error Log (`Logs/error.log`)**: Records errors, including file paths and reasons for failure.

---

## 🛠 Troubleshooting
### ❓ No Changes to Timestamps?
Ensure filenames contain valid date-time patterns. Files without valid patterns are skipped.

### ❓ ImportError: No module named 'pywintypes'
Run:
```sh
pip install pywin32
```

### ❓ Tkinter Not Found
If running on Linux and `tkinter` is missing, install it using:
```sh
sudo apt-get install python3-tk
```

---

## 🔮 Future Enhancements
- Support additional date formats.
- Add CLI options for non-GUI batch processing.
- Enhance cross-platform compatibility.
- Integrate with cloud storage solutions.

---

##  📖 Code Explanation
### **1. Language Support Setup**

#### **Language Configuration File Path**
```python
lang_path = os.path.join(os.getcwd(), "language.ini")
config = configparser.ConfigParser()
config.read(lang_path)
```

- **`os.path.join(os.getcwd(), "language.ini")`**:
  - Combines the current working directory (`os.getcwd()`) with the `language.ini` file name to form the complete path to the language configuration file.
  - This file determines the default language used in the program.
  
- **`configparser.ConfigParser()`**:
  - A Python module used to read and parse `.ini` configuration files.
  
- **`config.read(lang_path)`**:
  - Loads the `language.ini` file into the `config` object for further processing.

#### **Load Default Language**
```python
default_language = config.get("language", "default", fallback="en")
lang_folder = os.path.join(os.getcwd(), "lang", f"{default_language}.ini")
```

- **`config.get("language", "default", fallback="en")`**:
  - Fetches the default language specified in the `[language]` section under the `default` key of `language.ini`.
  - If the key or section is missing, it defaults to `"en"` (English).

- **`os.path.join(os.getcwd(), "lang", f"{default_language}.ini")`**:
  - Forms the path to the corresponding language file (e.g., `lang/en.ini` for English or `lang/vi.ini` for Vietnamese).

#### **Read Language File**
```python
lang_config = configparser.ConfigParser()
lang_config.read(lang_folder, encoding="utf-8")
```

- **`lang_config.read(lang_folder, encoding="utf-8")`**:
  - Loads the specific language `.ini` file (e.g., `en.ini`) and makes its translations available for the program.
  - UTF-8 encoding ensures support for special characters in translations.

### **2. Translation Function**

```python
def get_translation(key, fallback="", section="ui"):
    return lang_config.get(section, key, fallback=fallback)
```

- **Purpose**:
  - Retrieves a translated string from the language file.

- **Parameters**:
  - `key`: The specific text key to be translated (e.g., `help_title`).
  - `fallback`: A default value to use if the key is missing from the language file.
  - `section`: The section in the `.ini` file where the key resides (e.g., `ui` for user interface strings).

- **`lang_config.get()`**:
  - Looks up the `key` in the specified `section` of the loaded language file.
  - If the key is not found, the `fallback` value is returned.


### **3. `FileTimestampUpdater` Class**

This class handles the core functionality of updating file timestamps based on their filenames.

#### **Initialization**
```python
class FileTimestampUpdater:
    def __init__(self):
        self.project_dir = os.getcwd()
        self.log_directory = os.path.join(self.project_dir, "Logs")
        self.success_log_path = os.path.join(self.log_directory, "success.log")
        self.error_log_path = os.path.join(self.log_directory, "error.log")
        os.makedirs(self.log_directory, exist_ok=True)
```

- **Attributes**:
  - `self.project_dir`: The base directory of the project, obtained using `os.getcwd()`.
  - `self.log_directory`: Path to the directory where log files will be stored (`Logs`).
  - `self.success_log_path`: File path for storing successful operations (`Logs/success.log`).
  - `self.error_log_path`: File path for logging errors (`Logs/error.log`).

- **`os.makedirs(self.log_directory, exist_ok=True)`**:
  - Ensures the `Logs` directory exists. If it doesn’t, it creates it.


#### **Logging Messages**
```python
def log_message(self, message_key, log_file, **kwargs):
    message_template = get_translation(message_key, fallback=message_key)
    message = message_template.format(**kwargs)
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} - {message}\n")
```

- **Purpose**:
  - Writes log messages for both successful and failed operations.

- **Parameters**:
  - `message_key`: Key for the translated log message.
  - `log_file`: The specific log file to write to (e.g., `success.log` or `error.log`).
  - `kwargs`: Dynamic arguments to format the log message (e.g., `{filename}`, `{datetime}`).

- **Process**:
  - Retrieves the translation template using `get_translation()`.
  - Formats the template with the provided arguments.
  - Writes the formatted message to the specified log file with a timestamp.

#### **Extract Timestamp from Filename**
```python
def extract_datetime_from_filename(self, filename):
    patterns = [
        r".*?(\d{4})(\d{2})(\d{2})[_-](\d{2})(\d{2})(\d{2})",
        r".*?(\d{4})(\d{2})(\d{2})[_-](\d{2})(\d{2})",
    ]
    for pattern in patterns:
        match = re.search(pattern, os.path.splitext(filename)[0])
        if match:
            groups = match.groups()
            if len(groups) == 6:
                year, month, day, hour, minute, second = map(int, groups)
            elif len(groups) == 5:
                year, month, day, hour, minute = map(int, groups)
                second = 0
            return datetime(year, month, day, hour, minute, second)
    return None
```

- **Purpose**:
  - Extracts a valid timestamp from the filename using regular expressions.

- **Key Points**:
  - `patterns`: A list of regex patterns to match common timestamp formats.
  - `os.path.splitext(filename)[0]`: Strips the file extension, leaving only the base name for matching.
  - `datetime(year, month, day, hour, minute, second)`: Constructs a `datetime` object from the extracted values.

- **Supported Patterns**:
  - `YYYYMMDD_HHMMSS` (e.g., `20230811_154500`)
  - `YYYYMMDD_HHMM` (e.g., `20230811_1545`)

#### **Update File Timestamps**
```python
def update_file_timestamps(self, directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        new_datetime = self.extract_datetime_from_filename(filename)
        if new_datetime:
            new_timestamp = time.mktime(new_datetime.timetuple())
            os.utime(file_path, (new_timestamp, new_timestamp))
            # Win32 creation time update
            try:
                file_handle = win32file.CreateFile(...)
                win32file.SetFileTime(file_handle, pywintypes.Time(new_datetime), None, None)
                file_handle.Close()
                self.log_message("success_update", self.success_log_path, filename=filename, datetime=new_datetime)
            except Exception as e:
                self.log_message("error_update", self.error_log_path, filename=filename, error=e)
        else:
            self.log_message("invalid_file", self.error_log_path, filename=filename)
```

- **Purpose**:
  - Updates the creation and modification timestamps of files.

- **Process**:
  - Extracts the timestamp from the filename using `extract_datetime_from_filename`.
  - Updates the modification time using `os.utime`.
  - Uses `win32file.SetFileTime` to update the creation time on Windows systems.
  - Logs success or failure for each file.

### **4. GUI for Manual Timestamp Updates**

#### **Open GUI**
```python
def open_gui():
    ...
    calendar = Calendar(root, date_pattern="yyyy-mm-dd")
    ...
    apply_changes()
```

- **Purpose**:
  - Allows users to manually select a date and time for updating file timestamps via a graphical interface.

- **Key Components**:
  - `Calendar`: A widget for selecting dates.
  - `Spinbox`: Inputs for hours, minutes, and seconds.

#### **Apply Changes**
```python
def apply_changes():
    ...
    user_datetime = datetime(year, month, day, hour, minute, second)
    modifier.process_timestamp_updates(folder_path.get(), user_datetime)
```

- **Purpose**:
  - Collects user input and updates the timestamps for all files in the selected folder.

---

## 📄 License
```text
MIT License

Copyright (c) 2025 Nyakko Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

🎉 **Happy Organizing!** 🚀
