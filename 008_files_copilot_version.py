"""
008 - File Operations: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the File Operations exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Understand how to open and read files
- Learn different file reading methods
- Use pathlib for modern file path handling
- Master the 'with' statement for safe file operations
- Write and append to files
- Check file existence before operations
- Handle file errors gracefully

"""

# ============================================================================
# PART 1: Basic File Reading
# ============================================================================
# The open() function opens a file and returns a file object
# Mode 'r' = read (default mode)

print("=== PART 1: Basic File Reading ===\n")

# Basic file opening (manual close required)
file_path = 'my_file.txt'
file_obj = open(file_path, 'r')

# The file object is not the content itself
print(f"File object: {file_obj}")
print(f"Type: {type(file_obj)}")

# Remember to close the file when done
file_obj.close()

print()


# ============================================================================
# PART 2: Reading File Line by Line
# ============================================================================
# readline() reads one line at a time
# readlines() reads all lines into a list

print("=== PART 2: Reading Methods ===\n")

file_obj = open('my_file.txt', 'r')

# Method 1: readline() - reads one line
print("Using readline():")
ln = file_obj.readline()
print(f"First line: {ln}")
ln = file_obj.readline()
print(f"Second line: {ln}")

# Close and reopen to start from beginning
file_obj.close()

print("\nUsing readlines():")
file_obj = open('my_file.txt', 'r')

# Method 2: readlines() - reads all lines into a list
lns = file_obj.readlines()
print(f"All lines as list: {lns}")

# Loop through the lines
print("\nLooping through lines:")
for ln in lns:
    print(ln, end='')  # end='' because each line already has \n

file_obj.close()

print("\n")


# ============================================================================
# PART 3: Using pathlib for Path Handling
# ============================================================================
# pathlib provides object-oriented way to work with file paths
# More modern and cross-platform than using string paths

print("=== PART 3: pathlib Module ===\n")

from pathlib import Path

# Method 1: Absolute path (full path from root)
file_path = Path(r'C:\coag_temp\_F2026\1sem_prog\CYB-F26A-code\my_file.txt')
print(f"Absolute path: {file_path}")

# Get current working directory
print(f"Current working directory: {file_path.cwd()}")

# Method 2: Using current working directory
cwd = Path.cwd()
print(f"CWD: {cwd}")

# Join paths using joinpath()
file_path = cwd.joinpath('my_file.txt')
print(f"Joined path: {file_path}")

# Open and read using Path
file_obj = open(file_path, 'r')
print(f"First line: {file_obj.readline()}", end='')
file_obj.close()

print("\n")


# ============================================================================
# PART 4: The 'with' Statement (Context Manager)
# ============================================================================
# 'with' automatically closes the file when done
# This is the BEST PRACTICE for file operations

print("=== PART 4: Using 'with' Statement ===\n")

cwd = Path.cwd()
file_path = cwd.joinpath('test.txt')

# Old way (manual close)
print("Old way - manual close:")
f_obj = open(file_path, 'r')
print(f_obj.readline(), end='')
f_obj.close()

print("\n\nBest practice - with statement:")
# Best practice: with statement
with open(file_path, 'r') as f_obj:
    for line in f_obj:
        print(line, end='')
# File is automatically closed here!

print("\n")


# ============================================================================
# PART 5: File Opening Modes
# ============================================================================
# Different modes for opening files:
# 'r' = read (default)
# 'w' = write (creates new file, overwrites existing)
# 'a' = append (adds to end of file)
# 'r+' = read and write
# 'x' = exclusive creation (fails if file exists)

print("=== PART 5: File Opening Modes ===\n")

print("File modes:")
print("'r'  - Read only (default)")
print("'w'  - Write (overwrites existing)")
print("'a'  - Append to end")
print("'r+' - Read and write")
print("'x'  - Create new (error if exists)")

print()


# ============================================================================
# PART 6: Writing to Files - Append Mode
# ============================================================================
# Mode 'a' appends to the end of the file without erasing content

print("=== PART 6: Appending to Files ===\n")

# Append to file
with open('test.txt', 'a') as f_obj:
    f_obj.write('Hello from Python\n')
    f_obj.write('This line was appended\n')

print("Content added to test.txt")

# Read back to verify
print("\nCurrent content of test.txt:")
with open('test.txt', 'r') as f_obj:
    for line in f_obj:
        print(line, end='')

print("\n")


# ============================================================================
# PART 7: Writing to Files - Write Mode
# ============================================================================
# Mode 'w' creates a new file or OVERWRITES existing file

print("=== PART 7: Writing (Overwriting) Files ===\n")

# Write mode - OVERWRITES the file
with open('test2.txt', 'w') as f_obj:
    f_obj.write('Hello from Python AGAIN\n')
    f_obj.write('This is the second line\n')
    f_obj.write('This is the third line\n')

print("Created/overwrote test2.txt")

# Read back to verify
print("\nContent of test2.txt:")
with open('test2.txt', 'r') as f_obj:
    for line in f_obj:
        print(line, end='')

print("\n")


# ============================================================================
# PART 8: Writing Lists to Files
# ============================================================================
# writelines() writes a list of strings to a file

print("=== PART 8: Writing Lists to Files ===\n")

# Create a list of lines
lines = [
    "Line 1: Introduction\n",
    "Line 2: Body\n",
    "Line 3: Conclusion\n"
]

# Write the list to file
with open('list_output.txt', 'w') as f_obj:
    f_obj.writelines(lines)

print("Wrote list to list_output.txt")

# Read back to verify
print("\nContent of list_output.txt:")
with open('list_output.txt', 'r') as f_obj:
    content = f_obj.read()  # read() gets entire content as string
    print(content)

print()


# ============================================================================
# PART 9: Checking if File Exists
# ============================================================================
# Always check if a file exists before reading
# Use os.path.exists() or Path.exists()

print("=== PART 9: Checking File Existence ===\n")

import os

# Method 1: Using os.path.exists()
file_path = 'test.txt'
if os.path.exists(file_path):
    print(f"'{file_path}' exists!")
else:
    print(f"'{file_path}' does not exist")

# Method 2: Using pathlib
file_path = Path('test.txt')
if file_path.exists():
    print(f"'{file_path}' exists (checked with pathlib)!")
else:
    print(f"'{file_path}' does not exist")

# Check non-existent file
if os.path.exists('nonexistent.txt'):
    print("File exists")
else:
    print("'nonexistent.txt' does not exist")

print()


# ============================================================================
# PART 10: Read and Write Mode
# ============================================================================
# Mode 'r+' allows both reading and writing to the same file
# Mode 'a+' allows reading and appending

print("=== PART 10: Read and Write Mode ===\n")

file_path = 'numbers.txt'

# Create initial file with 0
if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write('0\n')
    print(f"Created {file_path} with initial value 0")

# Read, increment, and write back
with open(file_path, 'r+') as f:
    lines = f.readlines()  # Read all lines
    current_number = int(lines[-1].strip())  # Get last line, remove \n
    print(f"Current value: {current_number}")
    
    new_number = current_number + 1
    f.write(f'{new_number}\n')  # Append new number
    print(f"Wrote new value: {new_number}")

# Read back to verify
print("\nCurrent content:")
with open(file_path, 'r') as f:
    print(f.read())

print()


# ============================================================================
# PART 11: Practical Example - Run Counter
# ============================================================================
# A practical program that counts how many times it has been run

print("=== PART 11: Run Counter Example ===\n")

file_path = 'numbers2.txt'
isFile = os.path.exists(file_path)

if isFile:
    # File exists - read current count and increment
    with open(file_path, 'r+') as f:
        lns = f.readlines()
        run_count = int(lns[-1].strip())
        new_count = run_count + 1
        f.write(f'{new_count}\n')
        print(f"This program has run {new_count} times")
else:
    # File doesn't exist - create it with count 0
    with open(file_path, 'w') as f:
        f.write('0\n')
        print("First time running - created counter file")

print()


# ============================================================================
# PART 12: Error Handling with Files
# ============================================================================
# Always use try/except when working with files

print("=== PART 12: File Error Handling ===\n")

def safe_read_file(filename):
    """
    Safely reads a file with error handling.
    
    Parameters:
        filename: Name of the file to read
    
    Returns:
        File contents as string, or None if error occurs
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Test the function
print("Testing safe_read_file:")
content = safe_read_file('test.txt')
if content:
    print(f"Successfully read file (first 50 chars): {content[:50]}...")

content = safe_read_file('nonexistent.txt')
if content is None:
    print("Failed to read file (as expected)")

print()


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Read and Count Lines
Create a function that reads a file and returns the number of lines.

# def count_lines(filename):
#     try:
#         with open(filename, 'r') as f:
#             lines = f.readlines()
#             return len(lines)
#     except FileNotFoundError:
#         print(f"File '{filename}' not found")
#         return 0
# 
# count = count_lines('test.txt')
# print(f"Number of lines: {count}")


Exercise 2: Write Shopping List
Create a shopping list and write it to a file.

# shopping_list = ['apples', 'bananas', 'milk', 'bread', 'eggs']
# 
# with open('shopping_list.txt', 'w') as f:
#     for item in shopping_list:
#         f.write(f"{item}\n")
# 
# print("Shopping list saved!")


Exercise 3: Read and Filter
Read a file and print only lines that contain a specific word.

# def find_word_in_file(filename, word):
#     try:
#         with open(filename, 'r') as f:
#             for line in f:
#                 if word.lower() in line.lower():
#                     print(line, end='')
#     except FileNotFoundError:
#         print(f"File not found: {filename}")
# 
# find_word_in_file('test.txt', 'Python')


Exercise 4: Append Timestamp
Create a function that appends the current date/time to a file.

# from datetime import datetime
# 
# def log_timestamp(filename):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(filename, 'a') as f:
#         f.write(f"Log entry: {timestamp}\n")
# 
# log_timestamp('timestamps.txt')


Exercise 5: Copy File
Create a function that copies one file to another.

# def copy_file(source, destination):
#     try:
#         with open(source, 'r') as src:
#             content = src.read()
#         
#         with open(destination, 'w') as dst:
#             dst.write(content)
#         
#         print(f"Copied {source} to {destination}")
#         return True
#     except FileNotFoundError:
#         print(f"Source file '{source}' not found")
#         return False
#     except Exception as e:
#         print(f"Error: {e}")
#         return False
# 
# copy_file('test.txt', 'test_backup.txt')


Exercise 6: Count Words
Count how many words are in a file.

# def count_words(filename):
#     try:
#         with open(filename, 'r') as f:
#             content = f.read()
#             words = content.split()
#             return len(words)
#     except FileNotFoundError:
#         print(f"File not found: {filename}")
#         return 0
# 
# word_count = count_words('test.txt')
# print(f"Word count: {word_count}")


Challenge 1: User Database
Create a simple user database that stores usernames and emails.
Functions: add_user(), find_user(), list_all_users()

# def add_user(username, email):
#     with open('users.txt', 'a') as f:
#         f.write(f"{username}|{email}\n")
#     print(f"Added user: {username}")
# 
# def find_user(username):
#     try:
#         with open('users.txt', 'r') as f:
#             for line in f:
#                 parts = line.strip().split('|')
#                 if parts[0] == username:
#                     return parts[1]
#         return None
#     except FileNotFoundError:
#         return None
# 
# def list_all_users():
#     try:
#         with open('users.txt', 'r') as f:
#             for line in f:
#                 parts = line.strip().split('|')
#                 print(f"User: {parts[0]}, Email: {parts[1]}")
#     except FileNotFoundError:
#         print("No users found")
# 
# add_user('alice', 'alice@example.com')
# add_user('bob', 'bob@example.com')
# 
# email = find_user('alice')
# print(f"Alice's email: {email}")
# 
# list_all_users()


Challenge 2: Log Analyzer
Read a log file and generate statistics:
- Total entries
- Success vs failed attempts
- Most frequent IP address

# def analyze_logs(filename):
#     try:
#         total = 0
#         success_count = 0
#         failed_count = 0
#         ip_counts = {}
#         
#         with open(filename, 'r') as f:
#             for line in f:
#                 total += 1
#                 parts = line.strip().split('|')
#                 
#                 if len(parts) >= 4:
#                     ip = parts[1]
#                     status = parts[3]
#                     
#                     if status == 'success':
#                         success_count += 1
#                     else:
#                         failed_count += 1
#                     
#                     ip_counts[ip] = ip_counts.get(ip, 0) + 1
#         
#         print(f"Total entries: {total}")
#         print(f"Successful: {success_count}")
#         print(f"Failed: {failed_count}")
#         
#         if ip_counts:
#             most_frequent = max(ip_counts, key=ip_counts.get)
#             print(f"Most frequent IP: {most_frequent} ({ip_counts[most_frequent]} times)")
#     
#     except FileNotFoundError:
#         print(f"Log file not found: {filename}")
# 
# analyze_logs('access_log.txt')

"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. Opening Files:
   - open(filename, mode) returns a file object
   - Modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read/write)
   - Always close files with .close() or use 'with' statement

2. Reading Files:
   - readline(): reads one line at a time
   - readlines(): reads all lines into a list
   - read(): reads entire content as a string
   - Use for loop to iterate through lines

3. Writing Files:
   - write(): writes a string
   - writelines(): writes a list of strings
   - 'w' mode overwrites, 'a' mode appends
   - Remember to add \n for line breaks

4. Best Practices:
   - Use 'with' statement (automatic file closing)
   - Check file existence with os.path.exists()
   - Use pathlib for path handling
   - Always use try/except for error handling
   - Close files when done (automatic with 'with')

5. Common Patterns:
   - Read all: with open(file, 'r') as f: content = f.read()
   - Read lines: with open(file, 'r') as f: lines = f.readlines()
   - Write: with open(file, 'w') as f: f.write(text)
   - Append: with open(file, 'a') as f: f.write(text)

Remember: Files are persistent storage - handle them with care!
"""
