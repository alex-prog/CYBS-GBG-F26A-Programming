"""
004 - Dictionaries and Sets: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the Dictionaries and Sets exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Master f-string formatting for better output
- Review list and tuple operations
- Understand dictionaries: key-value pairs
- Learn dictionary methods and operations
- Understand sets and their unique properties
- Apply these data structures to real-world problems

"""

# ============================================================================
# PART 1: F-Strings - Modern String Formatting
# ============================================================================
# F-strings (formatted string literals) are the modern way to format strings
# Prefix with 'f' and use {} for variables/expressions

print("=== PART 1: F-String Formatting ===\n")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Different ways to print
print(my_list)
print(f'My list is: {my_list}.')
print('My list is: ' + str(my_list))  # Old way (concatenation)
print('My list is:', my_list, '.')     # Using commas

# F-string special features
print(f'{my_list=}')  # Prints variable name and value
print(f'{my_list*2}')  # Can evaluate expressions
x = f'This is my formatted string, {(3%2)=}'
print(x)

# Using f-strings for formatted output
print(f'2. Print the first element of the list: {my_list[0]}')
print(f'3. Print the last element of the list: {my_list[-1]}')
print(f'4. Print the first 4 elements: {my_list[:4]}')

second_list = my_list[-3:]
print(f'Last 3 elements: {second_list}')

print()


# ============================================================================
# PART 2: List Operations Review
# ============================================================================
# Review of list methods and operations

print("=== PART 2: List Operations Review ===\n")

my_list = ['cyber']
print(f'Type: {type(my_list)}')

# Building a list
my_list.append(2)
my_list.append(1)
my_list.append(3)
print(f'After appends: {my_list}')

my_list.append('cyber')
print(f'After appending cyber again: {my_list}')

# Finding and deleting
print(f'Index of first cyber: {my_list.index("cyber")}')

del my_list[0::4]  # Delete every 4th element starting at 0
print(f'After del my_list[0::4]: {my_list}')

my_list.sort(reverse=True)
print(f'After sort(reverse=True): {my_list}')
print(f'Reversed again: {my_list[::-1]}')

print()


# ============================================================================
# PART 3: Practical List Example - IP Addresses
# ============================================================================
# Working with real-world data: IP address logs

print("=== PART 3: Working with IP Lists ===\n")

ips = ['189.19.202.26', '124.124.86.154', '111.123.147.92', '191.194.49.89', 
       '191.194.49.89', '3.100.186.196', '17.102.131.131', '170.40.162.9', 
       '66.23.103.242', '203.207.124.71', '3.100.186.196', '170.194.124.70', 
       '3.100.186.196', '161.240.120.16', '37.161.17.14', '3.100.186.196', 
       '144.182.46.41', '3.100.186.196', '67.180.5.237', '182.44.178.202']

ips.append('8.8.8.8')
print(f'Added Google DNS: {ips[-1]}')
print(f'Total entries: {len(ips)}')
print(f'Last 5 IPs: {ips[-5:]}')

# Count occurrences
suspicious_ip = '3.100.186.196'
count = ips.count(suspicious_ip)
print(f"Counts of '{suspicious_ip}': {count}")
print(f"⚠️ This IP appears {count} times - possible security concern!")

print()


# ============================================================================
# PART 4: Tuple Operations and Conversion
# ============================================================================
# Tuples are immutable, but you can convert to list and back

print("=== PART 4: Tuple Operations ===\n")

# Method 1: Convert to list, modify, convert back
x = (1, 2, 3, 4, 5, "Sebastian")
print(f'Original tuple: {x}')

x = list(x)  # Convert to list
x.append('Alex')
x = tuple(x)  # Convert back to tuple
print(f'After conversion method: {x}')

# Method 2: Concatenate tuples (more efficient)
x = (1, 2, 3, 4, 5, "Sebastian")
x = x + ('Alex',)  # Note the comma for single-element tuple!
print(f'After concatenation: {x}')

print()


# ============================================================================
# PART 5: Dictionaries - Basics
# ============================================================================
# Dictionaries store key-value pairs
# Keys must be immutable (strings, numbers, tuples)
# Values can be anything

print("=== PART 5: Dictionary Basics ===\n")

# Creating and modifying dictionaries
d = {"te1": 'Sebi', 'te2': 'Alex'}
d['name'] = 'Bob'  # Add new key-value pair
print(f'Dictionary: {d}')
print(f'Number of keys: {len(d)}')
print(f'Length of te2 value: {len(d["te2"])}')

# Checking membership (checks keys, not values!)
print(f"'te2' in d: {'te2' in d}")
print(f"'Alex' in d: {'Alex' in d}")  # False - Alex is a value, not a key

print()


# ============================================================================
# PART 6: Dictionaries with Complex Values
# ============================================================================
# Dictionary values can be lists, other dictionaries, etc.

print("=== PART 6: Dictionaries with Lists ===\n")

d = {'a': [1, 2], 'b': [4, 5]}
print(f'Dictionary: {d}')
print(f"'b' in d: {'b' in d}")  # Check if key exists
print(f"5 in d['b']: {5 in d['b']}")  # Check if value in list
print(f"d['b']: {d['b']}")

# Keys can be numbers or tuples
d[8] = 42
print(f'After d[8] = 42: {d}')

d[(1, 2)] = 'bob'  # Tuple as key
print(f'After d[(1,2)] = bob: {d}')

# Important: Lists cannot be keys (they're mutable)
# d[[1,2]] = 'error'  # This would raise: TypeError: unhashable type: 'list'

print()


# ============================================================================
# PART 7: Dictionary References
# ============================================================================
# Understanding how dictionaries store references to objects

print("=== PART 7: Dictionary References ===\n")

my_list = [1, 2, 3]
d = {'a': my_list, 'b': [2, 1]}
print(f'Dictionary with my_list: {d}')

# Reassigning my_list doesn't change the dictionary
my_list = 'wow'
print(f"After my_list = 'wow': {d}")
print("The dictionary still has the original list!")

# But if we modify the list in place, it WOULD change
my_list = [1, 2, 3]
d = {'a': my_list, 'b': [2, 1]}
my_list.append(4)  # Modify in place
print(f'After my_list.append(4): {d}')
print("Now the dictionary changed because we modified the same list object!")

print()


# ============================================================================
# PART 8: Dictionary Methods
# ============================================================================
# Dictionaries have useful methods to access their contents

print("=== PART 8: Dictionary Methods ===\n")

d = {'a': 12, 'b': 4, 'c': 16}
print(f'Dictionary: {d}')

# Get all keys, values, or items
print(f'Keys: {d.keys()}')      # dict_keys(['a', 'b', 'c'])
print(f'Values: {d.values()}')  # dict_values([12, 4, 16])
print(f'Items: {d.items()}')    # dict_items([('a', 12), ('b', 4), ('c', 16)])

# Iterating over dictionary items
print('\nIterating over items:')
for item in d.items():
    print(item)  # Each item is a tuple (key, value)

print('\nUsing tuple unpacking:')
for key, value in d.items():
    print(f'{key} → {value}')

print()


# ============================================================================
# PART 9: More Dictionary Methods
# ============================================================================
# Additional useful dictionary methods

print("=== PART 9: Advanced Dictionary Methods ===\n")

d = {'username': 'alice', 'role': 'admin', 'active': True}
print(f'User info: {d}')

# get() - safely access values (returns None if key doesn't exist)
print(f"d.get('username'): {d.get('username')}")
print(f"d.get('email'): {d.get('email')}")  # None
print(f"d.get('email', 'N/A'): {d.get('email', 'N/A')}")  # Default value

# update() - merge dictionaries
new_info = {'email': 'alice@example.com', 'department': 'IT'}
d.update(new_info)
print(f'After update: {d}')

# pop() - remove and return value
role = d.pop('role')
print(f'Popped role: {role}')
print(f'After pop: {d}')

# clear() - remove all items
d_copy = d.copy()
d_copy.clear()
print(f'After clear: {d_copy}')
print(f'Original unchanged: {d}')

print()


# ============================================================================
# PART 10: Sets - Unique Collections
# ============================================================================
# Sets are unordered collections of unique elements
# Great for removing duplicates and set operations

print("=== PART 10: Sets ===\n")

# Creating sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(f'Set 1: {s1}')
print(f'Set 2: {s2}')

# Sets automatically remove duplicates
s3 = {1, 2, 2, 3, 3, 3, 4}
print(f'Set with duplicates: {s3}')  # {1, 2, 3, 4}

# Set operations
print(f'\nUnion (all elements): {s1 | s2}')
print(f'Intersection (common): {s1 & s2}')
print(f'Difference (in s1 but not s2): {s1 - s2}')
print(f'Symmetric difference: {s1 ^ s2}')

# Practical use: removing duplicates from list
ips_with_duplicates = ['192.168.1.1', '10.0.0.1', '192.168.1.1', '10.0.0.1']
unique_ips = list(set(ips_with_duplicates))
print(f'\nOriginal IPs: {ips_with_duplicates}')
print(f'Unique IPs: {unique_ips}')

# Set methods
s = {1, 2, 3}
s.add(4)
print(f'\nAfter add(4): {s}')
s.remove(2)
print(f'After remove(2): {s}')

# Membership testing (very fast in sets!)
print(f"3 in s: {3 in s}")
print(f"99 in s: {99 in s}")

print()


# ============================================================================
# PART 11: Practical Example - Access Control
# ============================================================================
# Using dictionaries and sets to manage user access

print("=== PART 11: Practical Example - Access Control ===\n")

# User database (dictionary)
users = {
    'alice': {'role': 'admin', 'department': 'IT', 'active': True},
    'bob': {'role': 'user', 'department': 'HR', 'active': True},
    'charlie': {'role': 'user', 'department': 'IT', 'active': False}
}

# Allowed IPs (set for fast lookup)
allowed_ips = {'192.168.1.100', '192.168.1.101', '10.0.0.50'}

# Check access
def check_access(username, ip_address):
    if username not in users:
        return "❌ User not found"
    
    user = users[username]
    
    if not user['active']:
        return "❌ Account disabled"
    
    if ip_address not in allowed_ips:
        return "❌ Unauthorized IP address"
    
    return f"✅ Access granted - Role: {user['role']}, Dept: {user['department']}"

# Test access control
print(check_access('alice', '192.168.1.100'))
print(check_access('charlie', '192.168.1.100'))
print(check_access('bob', '192.168.1.999'))

print()


# ============================================================================
# 🎯 EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: F-String Formatting
Create variables for name, age, and city. Use f-strings to print:
"My name is [name], I am [age] years old, and I live in [city]."

# name = 'Alice'
# age = 25
# city = 'Copenhagen'
# print(f'My name is {name}, I am {age} years old, and I live in {city}.')


Exercise 2: Dictionary Creation
Create a dictionary representing a book with keys: title, author, year, pages.
Print each value using the keys.

# book = {'title': 'Python Programming', 'author': 'John Doe', 
#         'year': 2024, 'pages': 350}
# print(f"Title: {book['title']}")
# print(f"Author: {book['author']}")
# print(f"Year: {book['year']}")
# print(f"Pages: {book['pages']}")


Exercise 3: Dictionary Methods
Create a dictionary of three fruits and their prices.
- Print all keys
- Print all values
- Add a new fruit
- Calculate the total price

# fruits = {'apple': 2.5, 'banana': 1.5, 'orange': 3.0}
# print(f'Fruits: {fruits.keys()}')
# print(f'Prices: {fruits.values()}')
# fruits['grape'] = 4.0
# total = sum(fruits.values())
# print(f'Total: ${total}')


Exercise 4: Sets - Remove Duplicates
Given this list of student IDs:
[101, 102, 103, 101, 104, 102, 105, 103]
Remove duplicates and print unique IDs.

# student_ids = [101, 102, 103, 101, 104, 102, 105, 103]
# unique_ids = list(set(student_ids))
# print(f'Unique student IDs: {sorted(unique_ids)}')


Exercise 5: Set Operations
Create two sets:
- security_team = {'Alice', 'Bob', 'Charlie'}
- dev_team = {'Bob', 'Diana', 'Eve'}
Find who is on both teams, and who is only on security team.

# security_team = {'Alice', 'Bob', 'Charlie'}
# dev_team = {'Bob', 'Diana', 'Eve'}
# both = security_team & dev_team
# security_only = security_team - dev_team
# print(f'Both teams: {both}')
# print(f'Security only: {security_only}')


Challenge: IP Access Logger
Create a dictionary to track IP access attempts:
- Key: IP address
- Value: number of attempts
Add functions to:
1. Record an access attempt
2. Check if IP has exceeded 5 attempts (potential attack)

# access_log = {}
# 
# def record_access(ip):
#     if ip in access_log:
#         access_log[ip] += 1
#     else:
#         access_log[ip] = 1
# 
# def check_threat(ip):
#     if ip in access_log and access_log[ip] > 5:
#         return f"⚠️ ALERT: {ip} has {access_log[ip]} attempts"
#     return f"✓ {ip} is within limits"
# 
# # Test it
# for _ in range(7):
#     record_access('192.168.1.100')
# record_access('10.0.0.1')
# 
# print(check_threat('192.168.1.100'))
# print(check_threat('10.0.0.1'))

"""


# ============================================================================
# 💡 KEY TAKEAWAYS
# ============================================================================
"""
1. F-Strings:
   - Modern formatting: f'text {variable}'
   - Can include expressions: f'{x + y}'
   - Debug format: f'{variable=}'

2. Dictionaries:
   - Key-value pairs: {'key': 'value'}
   - Keys must be immutable (str, int, tuple)
   - Fast lookup by key
   - Methods: keys(), values(), items(), get(), update(), pop()

3. Sets:
   - Unordered collection of unique elements
   - Fast membership testing
   - Operations: union (|), intersection (&), difference (-)
   - Great for removing duplicates

4. When to use what:
   - List: Ordered, can have duplicates, mutable
   - Tuple: Ordered, can have duplicates, immutable
   - Dictionary: Key-value pairs, fast lookup
   - Set: Unique elements, fast membership testing

Remember: Choose the right data structure for your specific needs!
"""
