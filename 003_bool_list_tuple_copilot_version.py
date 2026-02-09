"""
003 - Booleans, Lists, and Tuples: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the Booleans, Lists, and Tuples exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Understand boolean logic and logical operators
- Master lists: indexing, slicing, and modification
- Learn list methods: append, sort, index, count
- Understand tuples and their immutability
- Convert between lists and tuples
- Work with character codes (ord and chr)

"""

# ============================================================================
# PART 1: Boolean Logic and Logical Operators
# ============================================================================
# Boolean values: True or False
# Logical operators: and, or, not

print("=== PART 1: Boolean Logic ===\n")

# Example: Access Control System
is_logged_in = True
has_admin_rights = False
account_locked = True

has_access = is_logged_in and has_admin_rights and not account_locked

if has_access:
    print('Access Granted')
else:
    print('Access Denied')  # This will print

print(f"Logged in: {is_logged_in}")
print(f"Admin rights: {has_admin_rights}")
print(f"Account locked: {account_locked}")
print(f"Has access: {has_access}")

print("\n--- After unlocking account and granting admin ---\n")

# Now with proper credentials
is_logged_in = True
has_admin_rights = True
account_locked = False

has_access = is_logged_in and has_admin_rights and not account_locked

if has_access:
    print('Access Granted')  # This will print
else:
    print('Access Denied')

print(f"Has access: {has_access}")

print()


# ============================================================================
# PART 2: Lists - Basics and Indexing
# ============================================================================
# Lists are ordered, mutable collections
# Index from 0 (start) or -1 (end)

print("=== PART 2: Lists - Indexing ===\n")

#    0  1  2  3  4   5  6
#   -7 -6 -5 -4 -3  -2 -1
x = [1, 2, 4, 5, 7, 42, 3]

print(f"List: {x}")
print(f"x[5] = {x[5]}")    # 42 (6th element)
print(f"x[-2] = {x[-2]}")  # 42 (second from end)

print()


# ============================================================================
# PART 3: List Slicing
# ============================================================================
# Slicing: list[start:stop:step]
# Returns a new list with selected elements

print("=== PART 3: List Slicing ===\n")

#    0  1  2  3  4   5  6
x = [1, 2, 4, 5, 7, 42, 3]

# Basic slicing
print(f"x[0:4] = {x[0:4]}")  # [1, 2, 4, 5]
print(f"x[:4] = {x[:4]}")    # [1, 2, 4, 5] (start defaults to 0)
print(f"x[2:4] = {x[2:4]}")  # [4, 5]

# Slicing with step
print(f"x[::2] = {x[::2]}")    # [1, 4, 7, 3] (every 2nd element)
print(f"x[::-1] = {x[::-1]}")  # [3, 42, 7, 5, 4, 2, 1] (reversed)
print(f"x[::-2] = {x[::-2]}")  # [3, 7, 4, 1] (reversed, every 2nd)

# Advanced slicing
print(f"x[2:4][::-1] = {x[2:4][::-1]}")  # [5, 4] (slice then reverse)
print(f"x[3:1:-1] = {x[3:1:-1]}")        # [5, 4] (reverse from 3 to 1)

# Slicing with out-of-range indices
print(f"x[-3:] = {x[-3:]}")    # [42, 3] (last 3 elements)
print(f"x[-10:] = {x[-10:]}")  # Full list (starts at beginning)
print(f"x[:156] = {x[:156]}")  # Full list (stops at end)

print()


# ============================================================================
# PART 4: Modifying Lists
# ============================================================================
# Lists are mutable - you can change their contents

print("=== PART 4: Modifying Lists ===\n")

#    0  1  2  3  4   5  6
x = [1, 2, 4, 5, 7, 42, 3]
print(f"Original: {x}")

# Changing a single element
x[1] = 'two'
print(f"After x[1] = 'two': {x}")

x[1] = 2  # Change it back
print(f"After x[1] = 2: {x}")

# Appending elements using slice assignment
x[len(x):] = [-8, -9, -10]
print(f"After appending [-8,-9,-10]: {x}")

# Replacing a slice
x = [1, 2, 4, 5, 7, 42, 3]
x[2:4] = [-6, -6]
print(f"After x[2:4] = [-6, -6]: {x}")

# Deleting elements with empty slice
x[2:4] = []
print(f"After x[2:4] = []: {x}")

# Deleting with del keyword
del x[0]
print(f"After del x[0]: {x}")

print()


# ============================================================================
# PART 5: List Methods - append, extend, sort
# ============================================================================
# Lists have built-in methods for manipulation

print("=== PART 5: List Methods ===\n")

#    0  1  2  3  4   5  6
x = [1, 2, 4, 5, 7, 42, 3]

# append() - adds ONE element to the end
x.append('text')
print(f"After append('text'): {x}")

x.append([1, 2, 3, 4])  # Adds the list as a single element
print(f"After append([1,2,3,4]): {x}")

# += extends the list (adds each element)
x = [1, 2, 4, 5, 7, 42, 3]
x += [1, 2, 3, 4]
print(f"After x += [1,2,3,4]: {x}")

# sort() - sorts the list in place
x = [1, 2, 4, 5, 7, 42, 3]
x.sort()
print(f"After sort(): {x}")

# Sorting strings (case-sensitive!)
x = ['a', 'b', 'A', 'c']
x.sort()
print(f"Sorted strings: {x}")  # ['A', 'a', 'b', 'c']

# Why? Lowercase letters have higher ASCII values
if 'a' > 'A':
    print("'a' is greater than 'A' (lowercase > uppercase)")
else:
    print("'A' is greater than 'a'")

print()


# ============================================================================
# PART 6: Character Codes - ord() and chr()
# ============================================================================
# ord() converts character to ASCII/Unicode number
# chr() converts number to character

print("=== PART 6: Character Codes ===\n")

x = ord('c')
print(f"ord('c') = {x}")  # 99

x = ord('A')
print(f"ord('A') = {x}")  # 65

x = ord('a')
print(f"ord('a') = {x}")  # 97

# chr() - reverse of ord()
x = chr(65)
print(f"chr(65) = {x}")  # A

x = chr(128013)
print(f"chr(128013) = {x}")  # 🐍 (snake emoji)

print()


# ============================================================================
# PART 7: List Methods - index() and count()
# ============================================================================
# index() finds the position of an element
# count() counts how many times an element appears

print("=== PART 7: List Methods - index() and count() ===\n")

#    0  1  2  3  4   5  6  7  8  9
x = [1, 2, 4, 5, 7, 42, 3, 4, 4, 4]

# index() - returns the index of first occurrence
idx = x.index(42)
print(f"Index of 42: {idx}")  # 5

idx = x.index(4)
print(f"Index of 4: {idx}")  # 2 (first occurrence)

# If element not found, raises ValueError
# idx = x.index(999)  # Would raise ValueError

# count() - counts occurrences
count = x.count(4)
print(f"Count of 4: {count}")  # 4

count = x.count(999)
print(f"Count of 999: {count}")  # 0 (doesn't raise error)

print()


# ============================================================================
# PART 8: List Repetition
# ============================================================================
# Multiply a list to repeat it

print("=== PART 8: List Repetition ===\n")

x = [1, 2, 3]
y = x * 3
print(f"[1, 2, 3] * 3 = {y}")  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print()


# ============================================================================
# PART 9: Tuples - Immutable Sequences
# ============================================================================
# Tuples are like lists but IMMUTABLE (cannot be changed)
# Use parentheses () instead of brackets []

print("=== PART 9: Tuples ===\n")

# Creating tuples
x = (1,)  # Single element tuple (comma is required!)
print(f"Single element tuple: {x}")

x = (1, 2, 3, 4, 5, 6, 7, 8, 12)
print(f"Tuple: {x}")
print(f"Type: {type(x)}")

# Tuples can contain mixed types
x = (1, "two", 4.0, ["a", "b"], (5, 6))
print(f"Mixed tuple: {x}")

# Tuples are IMMUTABLE - cannot change elements
# x[2] = 'd'  # This gives an error: 'tuple' object does not support item assignment

# But you CAN access elements
print(f"x[1] = {x[1]}")  # "two"

# Tuples can be concatenated
y = (7, 8, 9)
z = (x + y,)  # Include comma to make it a tuple
print(f"Nested tuple: {z}")

print()


# ============================================================================
# PART 10: Converting Between Lists and Tuples
# ============================================================================
# Use list() and tuple() to convert between types

print("=== PART 10: List ↔ Tuple Conversion ===\n")

x = [1, 2, 3, 4]
print(f"List: {x}, Type: {type(x)}")

# Convert list to tuple
y = tuple(x)
print(f"Tuple: {y}, Type: {type(y)}")

# Convert tuple back to list
x = list(y)
print(f"Back to list: {x}, Type: {type(x)}")

print("\nWhy use tuples?")
print("- Faster than lists")
print("- Protect data from modification")
print("- Can be used as dictionary keys (lists cannot)")
print("- Use less memory")

print()


# ============================================================================
# 🎯 EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Boolean Logic
Create a login system that checks:
- User must be authenticated
- User must have verified email
- User must not be banned
Print whether login is successful.

# is_authenticated = True
# email_verified = False
# is_banned = False
# can_login = is_authenticated and email_verified and not is_banned
# print(f"Can login: {can_login}")


Exercise 2: List Slicing
Given the list [10, 20, 30, 40, 50, 60, 70, 80, 90]
- Get the first 3 elements
- Get the last 3 elements
- Get every other element
- Reverse the list

# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[:3])
# print(nums[-3:])
# print(nums[::2])
# print(nums[::-1])


Exercise 3: List Modification
Create a list [1, 2, 3, 4, 5]
- Change the 2nd element to 20
- Append the value 6
- Sort the list in descending order (hint: use sort(reverse=True))

# numbers = [1, 2, 3, 4, 5]
# numbers[1] = 20
# numbers.append(6)
# numbers.sort(reverse=True)
# print(numbers)


Exercise 4: List Methods
Create a shopping list: ['apple', 'banana', 'apple', 'orange', 'apple']
- Count how many times 'apple' appears
- Find the index of 'banana'
- Add 'grape' to the list

# shopping = ['apple', 'banana', 'apple', 'orange', 'apple']
# print(shopping.count('apple'))
# print(shopping.index('banana'))
# shopping.append('grape')
# print(shopping)


Exercise 5: Tuples
Create a tuple with your name, age, and favorite color
Try to print each element
(Remember: you can't modify tuples!)

# my_info = ('Alice', 25, 'blue')
# print(f"Name: {my_info[0]}")
# print(f"Age: {my_info[1]}")
# print(f"Color: {my_info[2]}")


Challenge: Character Code Cipher
Write code that:
1. Takes a string
2. Converts each character to its ord() value
3. Adds 1 to each value
4. Converts back to characters using chr()
This creates a simple Caesar cipher!

# message = "HELLO"
# encrypted = []
# for char in message:
#     code = ord(char)
#     encrypted.append(chr(code + 1))
# result = ''.join(encrypted)
# print(f"Original: {message}")
# print(f"Encrypted: {result}")

"""


# ============================================================================
# 💡 KEY TAKEAWAYS
# ============================================================================
"""
1. Boolean Logic:
   - and: both must be True
   - or: at least one must be True
   - not: reverses True/False

2. Lists:
   - Mutable (can be changed)
   - Use [] brackets
   - Methods: append(), sort(), index(), count()
   - Can be sliced with [start:stop:step]

3. Tuples:
   - Immutable (cannot be changed)
   - Use () parentheses
   - Faster and safer than lists
   - Single element: (x,) with comma

4. Conversions:
   - list(tuple) converts tuple to list
   - tuple(list) converts list to tuple

5. Character Codes:
   - ord(char) → number
   - chr(number) → character

Remember: Choose lists when you need to modify data, 
tuples when data should not change!
"""
