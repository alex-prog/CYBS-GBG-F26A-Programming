"""
006 - Control Flows: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the Control Flows exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Master if/elif/else conditional statements
- Understand match/case statements (Python 3.10+)
- Learn while loops for repetition
- Master for loops and iteration
- Use the range() function effectively
- Understand tuple unpacking in loops
- Apply control flow to real-world problems

"""

# ============================================================================
# PART 1: If/Elif/Else - Basic Conditionals
# ============================================================================
# Conditional statements let your program make decisions
# Structure: if condition: ... elif condition: ... else: ...

print("=== PART 1: If/Elif/Else Statements ===\n")

a = 100
b = 100
c = 3

# Find the maximum of three numbers
if a >= b and a >= c:
    print(f'{a=} is the largest')
elif b >= a and b >= c:
    print(f'{b=} is the largest')
else:
    print(f'{c=} is the largest')

# Python has a built-in max() function
print(f'Using max(): {max(a, b, c)}')

# Real-world example: Access levels
user_age = 25
if user_age >= 18:
    print('Access granted - Adult user')
elif user_age >= 13:
    print('Limited access - Teen user')
else:
    print('Access denied - Parental consent required')

print()


# ============================================================================
# PART 2: Match/Case - Pattern Matching (Python 3.10+)
# ============================================================================
# Match statements are like advanced if/elif chains
# Great for handling multiple specific values

print("=== PART 2: Match/Case Statements ===\n")

# Example 1: HTTP Version checker
request_line = 'HTTP/1.1'
match request_line:
    case 'HTTP/0.9':
        print('You need to upgrade your browser; we do not support version 0.9')
        # exit(-30)  # Would terminate program
    case 'HTTP/1.0':
        print('You are running version 1.0 therefore non-persistent')
    case 'HTTP/1.1':
        print('You are running version 1.1 therefore persistent')
    case 'HTTP/2.0':
        print('You are running version 2.0 - excellent!')
    case other:
        print(f'{other} is not a valid HTTP version')
        # exit('Bye!')

print()

# Example 2: Number matching with catch-all
x = 420
match x:
    case 0:
        print('it is 0')
    case 100:
        print('it is 100')
    case 42:
        print('it is the answer to everything')
    case default_value:  # Catch-all: matches anything
        print(f'it is {default_value}')

print()


# ============================================================================
# PART 3: While Loops - Condition-Based Repetition
# ============================================================================
# While loops repeat as long as a condition is True
# Be careful: infinite loops happen if condition never becomes False!

print("=== PART 3: While Loops ===\n")

# Example 1: Countdown timer
alert_timer = 5
print("Security Alert: System will lock in:")
while alert_timer > 0:
    print(f"{alert_timer} seconds...")
    alert_timer -= 1  # Same as: alert_timer = alert_timer - 1
print("System locked!")

print()

# Example 2: Counting from 0 to 10
c = 0
print("Counting to 10:")
while c <= 10:
    print(c, end=' ')
    c += 1  # Same as: c = c + 1
print("\nDone!")

print()

# Example 3: Iterating over a string with while
x = 'BobIsHere'
idx = 0
print(f"Characters in '{x}':")
while idx < len(x):
    print(f"Index {idx}: {x[idx]}")
    idx += 1

print()


# ============================================================================
# PART 4: String Methods - isdigit()
# ============================================================================
# isdigit() checks if all characters in a string are digits

print("=== PART 4: String Method - isdigit() ===\n")

# Test different strings
test_strings = ['helo1234', '1234', '1234b', '']

for string in test_strings:
    is_digit = string.isdigit()
    print(f'{string!r:15} is_digit: {is_digit}')

print()

# Checking each character
x = 'BobIsHere89'
print(f"Analyzing '{x}' character by character:")
for char in x:
    is_digit = char.isdigit()
    print(f'{char=:4} is_digit: {is_digit}')

print()


# ============================================================================
# PART 5: For Loops - Iterating Over Sequences
# ============================================================================
# For loops iterate over sequences (strings, lists, ranges, etc.)
# More common than while loops in Python!

print("=== PART 5: For Loops - Basics ===\n")

# Example 1: Iterating over a string
text = "Python"
print(f"Letters in '{text}':")
for char in text:
    print(char, end=' ')
print("\n")

# Example 2: Iterating over a list
fruits = ['apple', 'banana', 'cherry']
print("Fruits:")
for fruit in fruits:
    print(f"- {fruit}")

print()


# ============================================================================
# PART 6: The range() Function
# ============================================================================
# range() generates sequences of numbers
# Syntax: range(start, stop, step)

print("=== PART 6: The range() Function ===\n")

# range(stop) - from 0 to stop-1
print("range(5):", list(range(5)))  # [0, 1, 2, 3, 4]

# range(start, stop) - from start to stop-1
print("range(2, 7):", list(range(2, 7)))  # [2, 3, 4, 5, 6]

# range(start, stop, step) - with custom step
print("range(0, 11, 2):", list(range(0, 11, 2)))  # [0, 2, 4, 6, 8, 10]

# Negative step (counting down)
print("range(10, 0, -1):", list(range(10, 0, -1)))  # [10, 9, 8, ..., 1]

# Practical example: Scanning IP range
print('\nScanning IP range 192.168.1.x:')
for i in range(1, 6):  # Just first 5 for demo
    print(f'192.168.1.{i} - checking...')
print('... (and so on)')

print()


# ============================================================================
# PART 7: For Loops with Lists
# ============================================================================
# Different ways to iterate over lists

print("=== PART 7: For Loops with Lists ===\n")

x = [1, 5, 3, 6, 2, 9, 2, 4, 6, 8]

# Method 1: Iterate over elements directly
print("Method 1 - Direct iteration:")
for el in x:
    print(el, end=' ')
print("\n")

# Method 2: Iterate over indices
print("Method 2 - Using indices:")
for i in range(len(x)):
    print(f"Index {i}: value {x[i]}")

print()

# Method 3: enumerate() - get both index and value
print("Method 3 - Using enumerate():")
for i, value in enumerate(x):
    print(f"Index {i}: value {value}")

print()


# ============================================================================
# PART 8: Tuple Unpacking in Loops
# ============================================================================
# When iterating over tuples, you can unpack them directly

print("=== PART 8: Tuple Unpacking ===\n")

somelist = [(1, 2), (3, 7), (9, 5)]

# Method 1: Without unpacking
print("Without unpacking:")
result = 0
for item in somelist:
    print(f"Item: {item}, First: {item[0]}, Second: {item[1]}")
    result += item[0] * item[1]
print(f"Result: {result}\n")

# Method 2: With tuple unpacking (cleaner!)
print("With tuple unpacking:")
result = 0
for x, y in somelist:
    print(f"x={x}, y={y}, product={x*y}")
    result += x * y
print(f"Result: {result}")

print()


# ============================================================================
# PART 9: Loop Control - break and continue
# ============================================================================
# break: Exit the loop immediately
# continue: Skip to the next iteration

print("=== PART 9: Loop Control - break and continue ===\n")

# Example 1: break - stop when condition met
print("Finding first number divisible by 7:")
for num in range(1, 30):
    if num % 7 == 0:
        print(f"Found it: {num}")
        break  # Exit loop
    print(f"{num} - not divisible by 7")

print()

# Example 2: continue - skip certain iterations
print("Odd numbers between 1 and 10:")
for num in range(1, 11):
    if num % 2 == 0:  # If even
        continue  # Skip this iteration
    print(num, end=' ')
print("\n")

# Practical: Skip failed login attempts
print("Processing login attempts:")
login_attempts = ['alice', '', 'bob', '', 'charlie']
for username in login_attempts:
    if not username:  # Skip empty strings
        print("  Skipping empty attempt")
        continue
    print(f"  Processing login for: {username}")

print()


# ============================================================================
# PART 10: Nested Loops
# ============================================================================
# Loops inside loops - useful for 2D data, combinations, etc.

print("=== PART 10: Nested Loops ===\n")

# Example 1: Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j:2}", end="  ")
    print()  # Newline after each row

print()

# Example 2: Network scanning simulation
networks = ['192.168.1', '10.0.0']
ports = [80, 443, 22]

print("Port scanning:")
for network in networks:
    for host in range(1, 3):  # Just first 2 hosts for demo
        for port in ports:
            print(f"Scanning {network}.{host}:{port}")

print()


# ============================================================================
# !!!!! OPTIONAL !!!! - this is optional, we will not cover list comprehensions in class
# PART 11: List Comprehensions - Compact For Loops
# ============================================================================
# List comprehensions create lists in a single line
# Format: [expression for item in iterable if condition]

print("=== PART 11: List Comprehensions ===\n")

# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension way (more Pythonic!)
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares (comprehension): {squares}")

# With condition
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Practical: Filter valid IPs
all_ips = ['192.168.1.1', 'invalid', '10.0.0.1', '', '8.8.8.8']
valid_ips = [ip for ip in all_ips if '.' in ip and len(ip) > 6]
print(f"Valid IPs: {valid_ips}")

print()


# ============================================================================
# PART 12: Practical Examples - Real World Applications
# ============================================================================

print("=== PART 12: Practical Examples ===\n")

# Example 1: Password validation
# This example checks if a password meets certain security requirements
# We need to check: contains digit, uppercase, lowercase, and is at least 8 chars

password = "Pass123"
print(f"Checking password: {password}")

# Initialize boolean flags to track password requirements
has_digit = False
has_upper = False
has_lower = False

# Loop through each character in the password
for char in password:
    if char.isdigit():
        has_digit = True  # Found at least one digit
    elif char.isupper():
        has_upper = True  # Found at least one uppercase letter
    elif char.islower():
        has_lower = True  # Found at least one lowercase letter

# Check password length requirement
long_enough = len(password) >= 8

# Determine password strength based on all criteria
if has_digit and has_upper and has_lower and long_enough:
    print("Password is Strong")
elif long_enough:
    print("Password is Medium")
else:
    print("Password is Weak")

print()

# Example 2: Log analyzer
# This example analyzes security logs to detect suspicious login patterns
# We want to count failed login attempts per IP address

print("Analyzing security logs:")
log_entries = [
    ("192.168.1.100", "success"),
    ("10.0.0.50", "failed"),
    ("192.168.1.100", "success"),
    ("10.0.0.50", "failed"),
    ("10.0.0.50", "failed"),
]

# Create an empty dictionary to store failed attempt counts
# Key: IP address, Value: number of failed attempts
failed_attempts = {}

# Loop through each log entry using tuple unpacking
for ip, status in log_entries:
    if status == "failed":
        # If IP already exists in dictionary, increment count
        # If IP doesn't exist, get() returns 0, then we add 1
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

# Display results: loop through the dictionary
print("Failed login attempts by IP:")
for ip, count in failed_attempts.items():
    if count >= 3:
        # IP has 3 or more failed attempts - potential security threat
        print(f"  ALERT: {ip}: {count} failed attempts - BLOCKED")
    else:
        # IP has fewer than 3 failed attempts - just a warning
        print(f"  WARNING: {ip}: {count} failed attempts")

print()


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Grade Calculator
Write code that converts a numeric grade to a letter grade:
90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F

# grade = 85
# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print('B')
# elif grade >= 70:
#     print('C')
# elif grade >= 60:
#     print('D')
# else:
#     print('F')


Exercise 2: FizzBuzz
Print numbers 1-20, but:
- For multiples of 3, print "Fizz" instead
- For multiples of 5, print "Buzz" instead
- For multiples of both, print "FizzBuzz"

# for num in range(1, 21):
#     if num % 15 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)


Exercise 3: Sum of Even Numbers
Calculate the sum of all even numbers from 1 to 100.

# total = 0
# for num in range(2, 101, 2):  # Start at 2, step by 2
#     total += num
# print(f'Sum of even numbers 1-100: {total}')


Exercise 4: Character Counter
Count how many digits, letters, and spaces are in a string.

# text = "Hello World 123"
# digits = 0
# letters = 0
# spaces = 0
# 
# for char in text:
#     if char.isdigit():
#         digits += 1
#     elif char.isalpha():
#         letters += 1
#     elif char.isspace():
#         spaces += 1
# 
# print(f'Digits: {digits}, Letters: {letters}, Spaces: {spaces}')


Exercise 5: Find Maximum in List
Find the maximum value in a list without using max().

# numbers = [45, 12, 89, 23, 67, 34]
# maximum = numbers[0]
# for num in numbers:
#     if num > maximum:
#         maximum = num
# print(f'Maximum: {maximum}')


Exercise 6: Nested Loop - Coordinate Grid
Print all coordinates in a 3x3 grid (0,0) to (2,2).

# for x in range(3):
#     for y in range(3):
#         print(f'({x},{y})', end=' ')
#     print()



Challenge 1: Brute Force Login Detector
Given a list of login attempts (tuples of username and timestamp),
detect if any user has more than 3 failed attempts in a row.

# login_log = [
#     ('alice', '10:00', 'success'),
#     ('bob', '10:05', 'failed'),
#     ('bob', '10:06', 'failed'),
#     ('bob', '10:07', 'failed'),
#     ('bob', '10:08', 'failed'),
#     ('alice', '10:10', 'success'),
# ]
# 
# consecutive_fails = 0
# current_user = None
# 
# for user, time, status in login_log:
#     if user != current_user:
#         consecutive_fails = 0
#         current_user = user
#     
#     if status == 'failed':
#         consecutive_fails += 1
#         if consecutive_fails >= 3:
#             print(f'ALERT: {user} has {consecutive_fails} consecutive failed attempts!')
#     else:
#         consecutive_fails = 0

"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. Conditional Statements:
   - if/elif/else for decisions
   - match/case for pattern matching (Python 3.10+)

2. While Loops:
   - Repeat while condition is True
   - Risk of infinite loops
   - Good for unknown number of iterations

3. For Loops:
   - Iterate over sequences
   - More common than while in Python
   - Use range() for number sequences

4. Loop Control:
   - break: exit loop immediately
   - continue: skip to next iteration

5. Advanced Patterns:
   - Tuple unpacking: for x, y in list_of_tuples
   - List comprehensions: [expr for item in iterable if condition]
   - enumerate(): get index and value together
   - Nested loops: loop inside a loop

6. Best Practices:
   - Use for loops when you know the sequence
   - Use while loops when you don't know iteration count
   - Avoid infinite loops (ensure condition becomes False)
   - Use meaningful variable names in loops

Remember: Control flow is how you make programs intelligent!
"""
