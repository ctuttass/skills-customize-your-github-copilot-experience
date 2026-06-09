# 📘 Assignment: File I/O and Error Handling

## 🎯 Objective

Learn to read from and write to files in Python, and handle common runtime errors gracefully using `try/except/finally` blocks.

## 📝 Tasks

### 🛠️ Read and Display a File

#### Description
Write a function that opens a text file and prints its contents line by line.

#### Requirements
Completed program should:

- Accept a file path as a parameter
- Open the file using `open()` with the correct mode (`"r"`)
- Print each line with its line number (e.g. `1: Hello, world!`)
- Use a `try/except` block to catch `FileNotFoundError` and print a clear message like `Error: File 'data.txt' not found.`
- Example output for a file with two lines:
  ```
  1: Hello, Alice!
  2: Hello, Bob!
  ```

### 🛠️ Write and Append to a File

#### Description
Write two functions — one that creates a new file with provided content, and one that appends a line to an existing file.

#### Requirements
Completed program should:

- `write_file(path, lines)`: opens the file in write mode (`"w"`) and writes each item in `lines` as a separate line
- `append_to_file(path, line)`: opens the file in append mode (`"a"`) and adds the given line
- Use a `finally` block to ensure the file is always closed (or use a `with` statement)
- Raise a `ValueError` with a descriptive message if `lines` is empty when calling `write_file`
- Confirm success by printing `Written to <path>` or `Appended to <path>`

### 🛠️ Parse a CSV File

#### Description
Read the provided `sample-data.csv` file and compute a summary from its contents.

#### Requirements
Completed program should:

- Open and read `sample-data.csv` using Python's built-in `csv` module
- Skip the header row and parse each remaining row into a list of dictionaries
- Calculate and print the total number of records and the average value of the `score` column
- Handle `ValueError` if a `score` entry cannot be converted to a number, and skip that row with a warning
- Example output:
  ```
  Records loaded: 5
  Average score: 82.4
  Warning: Skipped row with invalid score: 'N/A'
  ```
