### Test Cases for TimestampUpdater Project

#### **1. Extracting Datetime from Filename**

**Test Case 1.1**
- **Description**: Extract datetime from a filename with pattern `YYYYMMDD_HHMMSS`.
- **Input**: `example_20250214_153000.txt`
- **Expected Output**: `datetime(2025, 2, 14, 15, 30, 0)`
- **Debugging Notes**: Ensure correct regex group matching.

**Test Case 1.2**
- **Description**: Extract datetime from a filename with pattern `YYYYMMDD-HHMM`.
- **Input**: `report_20230201-1430.doc`
- **Expected Output**: `datetime(2023, 2, 1, 14, 30, 0)`
- **Debugging Notes**: Validate fallback to `00` seconds.

**Test Case 1.3**
- **Description**: Invalid filename without datetime.
- **Input**: `invalid_file.txt`
- **Expected Output**: `None`
- **Debugging Notes**: Ensure no match logs an appropriate error.

**Test Case 1.4**
- **Description**: Extract datetime with mixed delimiters.
- **Input**: `data-20230415_121212.csv`
- **Expected Output**: `datetime(2023, 4, 15, 12, 12, 12)`
- **Debugging Notes**: Ensure multiple delimiters are supported.

#### **2. Updating File Timestamps**

**Test Case 2.1**
- **Description**: Update timestamp of a valid file with correct datetime.
- **Input**: `file_path: /test/example_20240101_123456.txt`
- **Expected Output**: File timestamp updated to `datetime(2024, 1, 1, 12, 34, 56)`.
- **Debugging Notes**: Verify file system changes reflect the updated timestamp.

**Test Case 2.2**
- **Description**: Invalid filename without datetime.
- **Input**: `file_path: /test/no_date_file.txt`
- **Expected Output**: Log error and skip the file.
- **Debugging Notes**: Ensure error is captured without breaking the loop.

**Test Case 2.3**
- **Description**: Directory contains a mix of valid and invalid files.
- **Input**: `/test/` with files: `file1_20250101_010101.txt, file2_invalid.doc`
- **Expected Output**: Valid file updated; invalid file logged as error.
- **Debugging Notes**: Check selective processing of valid files.

**Test Case 2.4**
- **Description**: Empty directory.
- **Input**: `/empty_directory/`
- **Expected Output**: No files processed; log appropriate message.
- **Debugging Notes**: Validate handling of empty directories.

#### **3. GUI Functionality**

**Test Case 3.1**
- **Description**: Select a folder through the GUI.
- **Input**: User selects `/test_directory/`
- **Expected Output**: Folder path stored and displayed in the GUI.
- **Debugging Notes**: Validate folder selection dialog and path storage.

**Test Case 3.2**
- **Description**: Apply changes with valid datetime.
- **Input**: 
  - Folder: `/test_folder/`
  - Selected Date: `2025-02-14`
  - Selected Time: `15:00:00`
- **Expected Output**: Timestamps of all files in the folder updated to the specified datetime.
- **Debugging Notes**: Ensure GUI properly triggers backend logic.

**Test Case 3.3**
- **Description**: Apply changes with no folder selected.
- **Input**: No folder selected.
- **Expected Output**: Error message displayed.
- **Debugging Notes**: Validate error handling for missing folder.

**Test Case 3.4**
- **Description**: Invalid time input.
- **Input**: 
  - Folder: `/test_folder/`
  - Selected Date: `2025-02-14`
  - Time: `25:00:00`
- **Expected Output**: Error message displayed.
- **Debugging Notes**: Ensure invalid time inputs are rejected.

#### **4. Language Support**

**Test Case 4.1**
- **Description**: Load English language file.
- **Input**: `default_language: en`
- **Expected Output**: All messages displayed in English.
- **Debugging Notes**: Validate parsing of `en.ini`.

**Test Case 4.2**
- **Description**: Load Vietnamese language file.
- **Input**: `default_language: vi`
- **Expected Output**: All messages displayed in Vietnamese.
- **Debugging Notes**: Ensure Vietnamese translations are loaded correctly.

**Test Case 4.3**
- **Description**: Missing language file.
- **Input**: `default_language: cn` but `cn.ini` missing.
- **Expected Output**: Fallback to English; log warning.
- **Debugging Notes**: Validate fallback mechanism.

**Test Case 4.4**
- **Description**: Corrupted language file.
- **Input**: `default_language: en` with `en.ini` corrupted.
- **Expected Output**: Error message displayed; program terminates.
- **Debugging Notes**: Ensure program exits gracefully.

#### **5. Error Handling**

**Test Case 5.1**
- **Description**: Missing directory for processing.
- **Input**: Invalid folder path: `/nonexistent_directory/`
- **Expected Output**: Error message logged; no files processed.
- **Debugging Notes**: Validate exception handling for missing directories.

**Test Case 5.2**
- **Description**: Invalid datetime format in filename.
- **Input**: File: `badfile_abc123.txt`
- **Expected Output**: Error logged; file skipped.
- **Debugging Notes**: Ensure robust regex validation.

**Test Case 5.3**
- **Description**: Permission denied when updating a file.
- **Input**: File with restricted permissions.
- **Expected Output**: Error logged; program continues.
- **Debugging Notes**: Ensure permission issues are gracefully handled.

**Test Case 5.4**
- **Description**: Large batch of files (>1000).
- **Input**: Directory with 1000+ files.
- **Expected Output**: All valid files processed; no memory leaks.
- **Debugging Notes**: Test performance and memory usage.

**Test Case 5.5**
- **Description**: File with no read permissions.
- **Input**: File path `/restricted/read_only_file.txt`.
- **Expected Output**: Log error; skip file.
- **Debugging Notes**: Ensure files without read permissions do not cause crashes.

**Test Case 5.6**
- **Description**: Invalid folder path with special characters.
- **Input**: Folder path `/invalid/?folder>`
- **Expected Output**: Log error; no processing performed.
- **Debugging Notes**: Validate handling of illegal characters in path.

**Test Case 5.7**
- **Description**: Log file directory missing.
- **Input**: Directory `/logs/` deleted before processing.
- **Expected Output**: Recreate logs directory; log messages normally.
- **Debugging Notes**: Validate log directory recreation mechanism.

**Test Case 5.8**
- **Description**: Non-ASCII characters in filename.
- **Input**: Filename `こんにちは_20230101.txt`
- **Expected Output**: Process file; update timestamp correctly.
- **Debugging Notes**: Ensure Unicode filenames are handled correctly.

**Test Case 5.9**
- **Description**: Processing nested directories.
- **Input**: Root directory with subfolders containing files.
- **Expected Output**: Skip subdirectories; process files only in root folder.
- **Debugging Notes**: Validate behavior with nested folder structures.

**Test Case 5.10**
- **Description**: Exceeding maximum path length on Windows.
- **Input**: File path exceeds 260 characters.
- **Expected Output**: Log error; skip file.
- **Debugging Notes**: Ensure compatibility with OS-specific path length limitations.

**Test Case 5.11**
- **Description**: Concurrent file modification.
- **Input**: File being updated by another process during timestamp change.
- **Expected Output**: Log error; program continues.
- **Debugging Notes**: Test concurrency handling robustness.

### Detailed Notes and Considerations for the Test Cases

#### **General Notes**
1. **Regex Validation**: Ensure that all patterns in `extract_datetime_from_filename` are rigorously tested to account for edge cases such as:
   - Files with no date information.
   - Files with partial datetime patterns.
   - Mixed delimiters in filenames (e.g., `_`, `-`, or spaces).

2. **Error Logging**:
   - Errors should be logged consistently in `error.log` with timestamps and relevant details.
   - Logs should include information about the file, error type, and any exception traceback.

3. **Unicode and Encoding**:
   - Test cases involving non-ASCII filenames (e.g., Japanese, Vietnamese) ensure the program handles Unicode characters gracefully.
   - Log files should support UTF-8 encoding to capture messages in different languages correctly.

4. **File Permissions**:
   - Ensure robust handling of files with restricted read, write, or access permissions.
   - Permission errors should not halt the entire process—files without issues should still be processed.

5. **Nested Directories**:
   - Currently, the program does not process files in subdirectories. It should explicitly log or notify users of skipped subdirectories to avoid confusion.

6. **Large Scale Testing**:
   - Performance should be monitored when processing large datasets (e.g., 1000+ files). Ensure there are no memory leaks, and processing times are reasonable.

7. **Compatibility**:
   - Validate OS-specific limitations, such as Windows path length (260 characters) or issues with special characters in Unix systems.

8. **Logging Directory**:
   - If the `Logs` directory is deleted or missing, the program should recreate it without user intervention to avoid logging failures.

---

#### **Notes for Specific Sections**

##### **Extracting Datetime from Filename**
- When testing patterns, ensure coverage for different formats, such as:
  - `YYYYMMDD_HHMMSS`
  - `YYYYMMDD-HHMM`
  - Partial datetime formats (e.g., `YYYY-MM-DD` without time).
- For files with no matches, ensure that the regex engine efficiently skips them without unnecessary computation.

##### **Updating File Timestamps**
- Verify that the system correctly updates:
  - File creation time.
  - Last modification time.
  - Last access time.
- Windows users should have `pywin32` installed and tested to ensure compatibility with file metadata updates.

##### **GUI Functionality**
- Ensure GUI components work seamlessly across different screen resolutions and DPI settings.
- Handle invalid inputs (e.g., incorrect time values like `25:00:00`) gracefully by displaying user-friendly error messages.

##### **Language Support**
- Each language file should contain fallback values for all keys. Missing keys should not result in crashes but revert to defaults.
- Test each `.ini` file for syntax errors or encoding issues.

##### **Error Handling**
- Handle scenarios like missing folders, missing log directories, or corrupted files gracefully without terminating the program unexpectedly.
- Clearly distinguish between recoverable and critical errors in the logs.

---

#### **Critical Considerations**
1. **Concurrency**:
   - Test how the system behaves when files are concurrently modified during processing. Add locks or retry mechanisms as necessary.

2. **Validation**:
   - Ensure user input (e.g., folder paths, timestamps) is validated to prevent crashes or undefined behavior.

3. **User Experience**:
   - For errors, provide actionable feedback (e.g., "The folder you selected does not exist. Please try again.").

4. **Testing Environment**:
   - Test in both CLI and GUI modes.
   - Validate behavior in different environments (e.g., Windows, macOS, Linux).