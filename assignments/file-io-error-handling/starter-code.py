# Starter Code for File I/O and Error Handling Assignment

import csv

# -------------------------------------------------------
# Task 1 – Read and display a file
# -------------------------------------------------------

def read_file(path):
    """Print each line of a file with its line number."""
    # TODO: Open the file in read mode using a try/except block
    # TODO: Catch FileNotFoundError and print a clear error message
    # TODO: Print each line as: "1: <line content>"
    pass


# -------------------------------------------------------
# Task 2 – Write and append to a file
# -------------------------------------------------------

def write_file(path, lines):
    """Write a list of lines to a file, overwriting existing content."""
    # TODO: Raise ValueError if lines is empty
    # TODO: Open the file in write mode and write each line
    # TODO: Use a finally block (or with statement) to ensure the file is closed
    # TODO: Print "Written to <path>" on success
    pass


def append_to_file(path, line):
    """Append a single line to an existing file."""
    # TODO: Open the file in append mode
    # TODO: Write the line followed by a newline character
    # TODO: Print "Appended to <path>" on success
    pass


# -------------------------------------------------------
# Task 3 – Parse a CSV file
# -------------------------------------------------------

def parse_csv(path):
    """Read sample-data.csv and print a summary of records and average score."""
    # TODO: Open the file using the csv module (csv.DictReader)
    # TODO: Skip invalid score values with a warning, don't crash
    # TODO: Print total number of records and average score
    pass


# -------------------------------------------------------
# Run all tasks
# -------------------------------------------------------

if __name__ == "__main__":
    # Task 1
    read_file("sample-data.csv")
    read_file("missing-file.txt")   # should print a friendly error

    # Task 2
    write_file("output.txt", ["Hello, Alice!", "Hello, Bob!"])
    append_to_file("output.txt", "Hello, Charlie!")
    read_file("output.txt")

    # Task 3
    parse_csv("sample-data.csv")
