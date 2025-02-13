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
    /modules           # Contains core modules
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
