"""
002 - Variables and Data Types (Primitives): GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the Variables and Data Types exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Understand what variables are and how to use them
- Learn about primitive data types: int, float, str, bool
- Master string operations and manipulation
- Learn string indexing and slicing
- Practice string methods

"""

# ============================================================================
# PART 1: Variables and Dynamic Typing
# ============================================================================
# Python is dynamically typed - variables can change type!
# The type() function tells us what data type a variable holds

print("=== PART 1: Variables and Dynamic Typing ===\n")

x = 443
print(x, type(x))  # 443 <class 'int'>

x = '443'  # Now x is a string!
print(x, type(x))  # 443 <class 'str'>

x = 4.0  # Now x is a float!
print(x, type(x))  # 4.0 <class 'float'>

x = True  # Now x is a boolean!
print(x, type(x))  # True <class 'bool'>

print()


# ============================================================================
# PART 2: Print Function Advanced Features
# ============================================================================
# The print() function has special parameters: sep and end

print("=== PART 2: Print Features ===\n")

# sep = separator (what goes between items)
print(15, 'bob and alice', 16.2, True, sep=' | ')
print(15, 'bob and alice', 16.2, True, sep='\n')  # \n = newline

# end = what comes at the end (default is newline)
print(10, end=' ')
print(20, end=' ')
print(30, end=' ')
print(40, end='\n\n')  # End with double newline


# ============================================================================
# PART 3: String Basics and Indexing
# ============================================================================
# Strings are sequences of characters
# Each character has an index (position) starting at 0

print("=== PART 3: String Indexing ===\n")

my_name = 'Alex Gh'
print(my_name)
print("First character:", my_name[0])  # A
print("Character at index 5:", my_name[5])  # G

# Strings have length
x = "Cybersikkerhed"
print(f"Length of '{x}':", len(x))  # 14 characters
print("Last character:", x[13])  # d (index 13 is the 14th character)

# Special characters use backslash (\)
y = 'aab \tasa \\'  # \t = tab, \\ = backslash
print("String with special chars:", y)
print("Length:", len(y))  # Count the characters!

print()


# ============================================================================
# PART 4: String Operations
# ============================================================================
# You can combine (concatenate) strings with +
# You can repeat strings with *

print("=== PART 4: String Operations ===\n")

# Concatenation (joining strings)
f_name = 'Alex'
l_name = 'Gh'
name = f_name + ' ' + l_name
print("Full name:", name)
print("Same result:", f_name, l_name)  # print adds spaces automatically

# Repetition (repeating strings)
c = 'Bob'
cc = c * 20
print("Repeated name:", cc)
print("Length:", len(cc))  # 3 * 20 = 60

x = 'A' * 513
print("513 A's:", x)
print("Length:", len(x))

print()


# ============================================================================
# PART 5: String Membership (in operator)
# ============================================================================
# Check if a character or substring is inside a string with 'in'

print("=== PART 5: String Membership ===\n")

print('a' in 'hello')      # False - no 'a' in 'hello'
print('l' in 'hello')      # True - 'l' is in 'hello'
print('hell' in 'hello')   # True - 'hell' is part of 'hello'
print('Hell' in 'hello')   # False - case sensitive!

print()


# ============================================================================
# PART 6: Negative Indexing
# ============================================================================
# Negative indices count from the end: -1 is last, -2 is second to last

print("=== PART 6: Negative Indexing ===\n")

first_name = 'Bob'
last_name = 'Spongey'
name = first_name + ' ' + last_name
print("Name:", name)

length = len(name)
print("Length:", length)

# Two ways to get the last character
print("Last char (positive):", name[length - 1])  # y
print("Last char (negative):", name[-1])          # y

#    0 1 2 3 4 5
#    a b c D E F
#   -6-5-4-3-2-1
x = 'abcDEF'
print("\nPositive and negative indexing:")
print("x[2]:", x[2])       # c
print("x[-2]:", x[-2])     # E
print("x[4]:", x[4])       # E
print("x[-6]:", x[-6])     # a (first character)
print("x[-len(x)]:", x[-len(x)])  # a (also first character)

print()


# ============================================================================
# PART 7: String Slicing
# ============================================================================
# Slicing lets you extract parts of a string
# Format: string[start:stop:step]

print("=== PART 7: String Slicing ===\n")

#    0123456
x = 'abcDEF'

# Basic slicing
print("x[0:3]:", x[0:3])   # abc (from 0 up to but not including 3)
print("x[:3]:", x[:3])     # abc (same - start defaults to 0)
print("x[3:]:", x[3:])     # DEF (from 3 to end)

# Slicing with step
print("x[::2]:", x[::2])   # acE (every 2nd character)
print("x[::-1]:", x[::-1]) # FEDcba (reversed!)
print("x[::-2]:", x[::-2]) # FDb (reversed, every 2nd)

print()


# ============================================================================
# PART 8: String Methods - Split and Join
# ============================================================================
# split() breaks a string into a list
# join() combines a list into a string

print("=== PART 8: Split and Join ===\n")

x = "Cybersikkerhed på EK"
my_list = x.split()  # Splits on whitespace by default
print("Split by spaces:", my_list)
print("Third word:", my_list[2])

# Split by custom delimiter
xx = '10|192.168.2.3|78|2026-02-02'
uu = xx.split('|')
print("\nSplit by |:", uu)
print("Last item:", uu[-1])
print("IP address:", uu[1])

# Split by multi-character delimiter
xx = '10@|@192.168.2.3@|@78@|@2026-02-02'
oo = xx.split('@|@')
print("\nSplit by @|@:", oo)

# Join - opposite of split
new_log = ' '.join(oo)
print("Joined with spaces:", new_log)

print()


# ============================================================================
# PART 9: String Methods - Transformation and Search
# ============================================================================
# Strings have many built-in methods for manipulation

print("=== PART 9: String Methods ===\n")

x = '   alice bob       \n'
print("Original:", repr(x))  # repr shows the exact string

# Case transformation
x_allcaps = x.upper()
print("Upper:", x_allcaps)

x_nice_name = x.title()
print("Title:", x_nice_name)

# Search methods
print("Find 'bob':", x.find('bob'))    # Returns index or -1
print("Index 'bob':", x.index('bob'))  # Returns index or raises error

# Cleaning whitespace
xx = x.strip()  # Remove leading/trailing whitespace
print("Stripped:", repr(xx))

print()


# ============================================================================
# PART 10: Escape Characters and Raw Strings
# ============================================================================
# Backslash (\) is used for special characters
# Use double backslash (\\) for literal backslash

print("=== PART 10: Escape Characters ===\n")

# WRONG: \t and \n are special characters
file_location_bad = 'C:\test\new.doc'
print("BAD (has escape chars):", file_location_bad)

# RIGHT: Use double backslash
file_location_good = 'C:\\www\\test\\new.doc'
print("GOOD (escaped properly):", file_location_good)

# Common escape sequences:
# \n = newline
# \t = tab
# \\ = backslash
# \' = single quote
# \" = double quote

print()


# ============================================================================
# 🎯 EXERCISES
# ============================================================================
"""
Practice what you've learned with these exercises!

Exercise 1: Variable Practice
Create variables for your favorite number, favorite color, and whether you
like programming. Print each one with its type.

# fav_num = 
# fav_color = 
# likes_programming = 
# print(fav_num, type(fav_num))
# print(fav_color, type(fav_color))
# print(likes_programming, type(likes_programming))


Exercise 2: String Indexing
Create a variable with your full name. Print:
- The first character
- The last character (using negative index)
- The length of your name

# full_name = 
# print("First:", full_name[0])
# print("Last:", full_name[-1])
# print("Length:", len(full_name))


Exercise 3: String Slicing
With the string "Python Programming":
- Extract "Python"
- Extract "Programming"
- Reverse the entire string

# text = "Python Programming"
# print(text[:6])
# print(text[7:])
# print(text[::-1])


Exercise 4: Split and Join
You have this log entry: "2026-02-02|ERROR|Database connection failed"
Split it by | and print each part separately.

# log = "2026-02-02|ERROR|Database connection failed"
# parts = log.split('|')
# print("Date:", parts[0])
# print("Level:", parts[1])
# print("Message:", parts[2])


Exercise 5: String Methods
Clean up this messy input: "  hello WORLD  \n"
- Remove whitespace
- Convert to lowercase
- Check if "world" is in the cleaned string

# messy = "  hello WORLD  \n"
# clean = messy.strip().lower()
# print(clean)
# print('world' in clean)


Challenge: Create a program that takes a person's name as input,
then prints it in various formats (uppercase, lowercase, title case,
reversed, with stars around it, etc.)

"""


# ============================================================================
# 💡 KEY TAKEAWAYS
# ============================================================================
"""
1. Variables can hold different types: int, float, str, bool
2. Python is dynamically typed - types can change
3. Strings are indexed starting at 0
4. Negative indices count from the end (-1 is last)
5. Slicing format: [start:stop:step]
6. Use split() to break strings, join() to combine
7. Many string methods available: upper(), lower(), strip(), find(), etc.
8. Use \\ for literal backslash in strings

Remember: Practice is key to mastering these concepts!
"""
