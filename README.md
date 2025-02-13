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
