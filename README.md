# 📌 File Timestamp Updater

🚀 **Version:** 1.0  
📧 **Contact:** [miko@wibu.me](mailto:miko@wibu.me)

---

## 📖 Overview
This script updates file timestamps based on their filenames, using specific date-time formats. It is particularly useful when organizing files by their creation or modification dates.

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
pip install pywin32
```

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

If a filename contains one of these formats, the extracted date-time is used to update the file's timestamps.

### ⏳ 3. Update File Timestamps
- The script modifies the **last modified time** and **creation time** of each file based on the extracted timestamp.
- It logs successful updates and errors in `Logs/success.log` and `Logs/error.log`.

---

## ✅ Naming Files Correctly
To ensure the script works properly, rename files to include a timestamp in the following format:
✅ **Correct:** `photo_20250302_110320.jpg`  
✅ **Correct:** `document_20250302_1103.pdf`  
❌ **Incorrect:** `photo_110320.jpg` (missing full date)  
❌ **Incorrect:** `document_2025-03-02.pdf` (missing time information)  

---

## 📜 Logging
- **✅ Success Log (`Logs/success.log`)**: Records files that were successfully updated.
- **❌ Error Log (`Logs/error.log`)**: Logs files that failed to be processed, including error details.

---

## 🛠 Troubleshooting
### ❓ No Changes to Timestamps?
Ensure filenames contain a valid date-time pattern. If the script does not find a match, the file is skipped.

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
- Support for additional date formats.
- CLI options for batch processing without GUI.
- Cross-platform compatibility.

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
