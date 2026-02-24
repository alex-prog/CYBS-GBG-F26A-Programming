"""
007 - Functions and Exception Handling: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the Functions and Exception Handling exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Understand how to define and call functions
- Learn about function parameters and return values
- Master type hints for better code clarity
- Use isinstance() for type checking
- Handle errors gracefully with try/except blocks
- Understand different exception types

"""

# ============================================================================
# PART 1: Functions - Basic Definition
# ============================================================================
# Functions are reusable blocks of code
# Define with 'def', call by name with arguments

print("=== PART 1: Basic Functions ===\n")

# Simple function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

print()


# ============================================================================
# PART 2: Functions with Multiple Parameters
# ============================================================================
# Functions can take multiple parameters and perform validation

print("=== PART 2: Functions with Validation ===\n")

def password_checker(password, minimum_length):
    """
    Checks if a password meets length requirements.
    
    Parameters:
        password: The password string to check
        minimum_length: Minimum required length (must be between 6 and 64)
    """
    # First, validate the minimum_length parameter itself
    if 64 >= minimum_length >= 6:
        pass  # Valid range, continue
    else:
        print('Minimum length not ok (must be 6-64)')
        return  # Exit function early
    
    # Now check if the password meets the minimum length
    if len(password) >= minimum_length:
        print(f'Password ok - {len(password)} characters')
    else:
        print(f'Password too short - needs at least {minimum_length} characters')

# Test the function
password_checker('aa', 3)  # minimum_length too low
password_checker('MySecurePass', 8)  # Good password
password_checker('aa', 69)  # minimum_length too high

print()


# ============================================================================
# PART 3: Functions with Return Values
# ============================================================================
# Functions can return values using the 'return' keyword
# You can specify the return type with type hints (-> type)

print("=== PART 3: Functions with Return Values ===\n")

def add_numbers(a, b) -> int:
    """
    Adds two numbers and returns the result.
    
    Parameters:
        a: First number
        b: Second number
    
    Returns:
        int: The sum of a and b
    """
    total = a + b
    return total

# Call the function and store the result
x = add_numbers(20, 30)
print(f"Result: {x}, Type: {type(x)}")

# You can also use the result directly
result = add_numbers(100, 50)
print(f"100 + 50 = {result}")

print()


# ============================================================================
# PART 4: Type Checking with isinstance()
# ============================================================================
# isinstance() checks if a variable is of a specific type
# Useful for validation and preventing errors

print("=== PART 4: Type Checking ===\n")

# Testing isinstance() with different types
print(f'isinstance("kk", int): {isinstance("kk", int)}')    # False
print(f'isinstance("kk", str): {isinstance("kk", str)}')    # True
print(f'isinstance(["kk"], list): {isinstance(["kk"], list)}')  # True
print(f'isinstance(42, int): {isinstance(42, int)}')        # True
print(f'isinstance(42, str): {isinstance(42, str)}')        # False

print()


# ============================================================================
# PART 5: Functions with Type Validation
# ============================================================================
# Combining functions with isinstance() for robust input validation

print("=== PART 5: Functions with Type Validation ===\n")

def string_checker(string) -> bool:
    """
    Checks if the input is a string.
    
    Parameters:
        string: Value to check
    
    Returns:
        bool: True if input is a string, False otherwise
    """
    if isinstance(string, str):
        return True
    else:
        return False

# Test with different types
password1 = 12345
password2 = '12345'

print(f'Is password1 ({password1}) a string? {string_checker(password1)}')
print(f'Is password2 ({password2}) a string? {string_checker(password2)}')

print()


# ============================================================================
# PART 6: Exception Handling - Why We Need It
# ============================================================================
# Without exception handling, errors stop the entire program

print("=== PART 6: Why Exception Handling? ===\n")

print("Without exception handling:")
# This would crash the program:
# print(5/0)
print("(Code commented out - would cause: ZeroDivisionError: division by zero)")

print("\nProgram continues after the error is avoided...")

print()


# ============================================================================
# PART 7: Basic Exception Handling
# ============================================================================
# try/except blocks catch errors and let the program continue

print("=== PART 7: Basic try/except ===\n")

print("Attempting division by zero with exception handling:")
try:
    print(5/0)  # This will cause an error
except Exception as e:
    print(f"Caught an error: {e}")

print("This is a very important line that still executes!")

print()


# ============================================================================
# PART 8: Multiple Exception Types
# ============================================================================
# You can handle different exceptions differently

print("=== PART 8: Handling Different Exception Types ===\n")

# Example 1: Catching specific exception
print("Example 1 - Catching ZeroDivisionError:")
try:
    print(5/0)
    x = "cyber"
    x = int(x)  # This won't run because of the error above
except ZeroDivisionError:
    print("Error: You can't divide by zero")
except:
    print("Error: Some other general error")

print()

# Example 2: Multiple possible errors
print("Example 2 - Multiple errors possible:")
try:
    # print(5/0)  # ZeroDivisionError
    x = "cyber"
    x = int(x)  # ValueError - can't convert "cyber" to int
except ZeroDivisionError:
    print("Error: You can't divide by zero")
except ValueError as e:
    print(f"Error: Invalid value conversion - {e}")
except:
    print("Error: Some other general error")

print()


# ============================================================================
# PART 9: General Exception Handling
# ============================================================================
# Catching any exception with Exception

print("=== PART 9: General Exception Handling ===\n")

try:
    # print(5/0)  # Commented out
    x = "cyber"
    x = int(x)  # This will cause ValueError
except Exception as error:
    print(f"Some error occurred: {error}")

print()


# ============================================================================
# PART 10: Practical Exception Handling Examples
# ============================================================================
# Real-world examples of exception handling

print("=== PART 10: Practical Examples ===\n")

# Example 1: Safe user input
def get_integer_input(prompt):
    """
    Safely get integer input from user.
    Keeps asking until valid input is received.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid integer")

# Example usage (commented out for automated testing):
# age = get_integer_input("Enter your age: ")
# print(f"You are {age} years old")

# Example 2: Safe file operations
def safe_divide(a, b):
    """
    Safely divides two numbers with error handling.
    
    Parameters:
        a: Numerator
        b: Denominator
    
    Returns:
        Result of division or None if error occurs
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None

# Test the safe divide function
print("Testing safe_divide:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

print()


# ============================================================================
# PART 11: try/except/else/finally
# ============================================================================
# Complete exception handling structure

print("=== PART 11: Complete Exception Handling ===\n")

def process_number(num_str):
    """
    Demonstrates complete try/except/else/finally structure.
    """
    try:
        # Try to convert and process
        number = int(num_str)
        result = 100 / number
    except ValueError:
        print(f"Error: '{num_str}' is not a valid number")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero")
    else:
        # Only runs if NO exception occurred
        print(f"Success: 100 / {number} = {result}")
    finally:
        # ALWAYS runs, whether exception occurred or not
        print(f"Finished processing '{num_str}'")
    print()

# Test with different inputs
process_number("10")     # Success
process_number("0")      # ZeroDivisionError
process_number("abc")    # ValueError

print()


# ============================================================================
# PART 12: Best Practices
# ============================================================================

print("=== PART 12: Best Practices ===\n")

# Best Practice 1: Be specific with exceptions
def example_specific():
    """Catch specific exceptions first, general ones last."""
    try:
        x = int("not a number")
    except ValueError:
        print("Specific: ValueError caught")
    except Exception:
        print("General: Some other exception")

example_specific()

# Best Practice 2: Don't hide errors silently
def example_silent():
    """Bad practice - silently catching errors."""
    try:
        result = 10 / 0
    except:
        pass  # BAD: Error is hidden!
    print("Continues without knowing an error occurred")

# Best Practice 3: Use exceptions for exceptional cases
def example_good_validation(age):
    """Use validation for expected checks, exceptions for unexpected errors."""
    # Good: Validate expected ranges
    if age < 0 or age > 150:
        print("Invalid age range")
        return False
    
    # Use exceptions for unexpected errors
    try:
        # Some operation that might fail unexpectedly
        age_string = str(age)
        return True
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

print()


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Simple Function
Create a function that takes a name and age, and prints a greeting.

# def greet_person(name, age):
#     print(f"Hello {name}, you are {age} years old")
# 
# greet_person("Alice", 25)


Exercise 2: Function with Return Value
Create a function that calculates the area of a rectangle.

# def calculate_area(length, width) -> float:
#     return length * width
# 
# area = calculate_area(5, 3)
# print(f"Area: {area}")


Exercise 3: Type Checking
Create a function that checks if input is a list.

# def is_list(value) -> bool:
#     return isinstance(value, list)
# 
# print(is_list([1, 2, 3]))  # True
# print(is_list("hello"))    # False


Exercise 4: Exception Handling
Create a function that safely converts a string to float.

# def safe_float_conversion(value):
#     try:
#         return float(value)
#     except ValueError:
#         print(f"Cannot convert '{value}' to float")
#         return None
# 
# print(safe_float_conversion("3.14"))
# print(safe_float_conversion("abc"))


Exercise 5: Password Validator
Create a function that validates passwords with these rules:
- At least 8 characters
- Contains at least one digit
- Returns True if valid, False otherwise

# def validate_password(password) -> bool:
#     if len(password) < 8:
#         print("Password too short")
#         return False
#     
#     has_digit = False
#     for char in password:
#         if char.isdigit():
#             has_digit = True
#             break
#     
#     if not has_digit:
#         print("Password must contain at least one digit")
#         return False
#     
#     print("Password is valid")
#     return True
# 
# validate_password("Pass123")
# validate_password("short")


Exercise 6: Safe Dictionary Access
Create a function that safely gets a value from a dictionary.

# def safe_dict_get(dictionary, key, default=None):
#     try:
#         return dictionary[key]
#     except KeyError:
#         print(f"Key '{key}' not found, returning default: {default}")
#         return default
# 
# data = {"name": "Alice", "age": 25}
# print(safe_dict_get(data, "name"))
# print(safe_dict_get(data, "email", "no-email@example.com"))


Challenge 1: Login System
Create a login function that:
- Takes username and password
- Checks if username exists in a user database (dictionary)
- Validates password
- Handles errors gracefully
- Returns True if successful, False otherwise

# users = {
#     "alice": "Pass123",
#     "bob": "SecureP@ss"
# }
# 
# def login(username, password) -> bool:
#     try:
#         if not isinstance(username, str) or not isinstance(password, str):
#             print("Error: Username and password must be strings")
#             return False
#         
#         if username not in users:
#             print("Error: User not found")
#             return False
#         
#         if users[username] == password:
#             print(f"Welcome {username}!")
#             return True
#         else:
#             print("Error: Incorrect password")
#             return False
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return False
# 
# login("alice", "Pass123")
# login("alice", "wrong")
# login("charlie", "Pass123")


Challenge 2: Calculator with Error Handling
Create a calculator function that:
- Takes two numbers and an operation (+, -, *, /)
- Performs the operation
- Handles all possible errors
- Returns the result or None if error

# def calculator(num1, num2, operation):
#     try:
#         if operation == '+':
#             return num1 + num2
#         elif operation == '-':
#             return num1 - num2
#         elif operation == '*':
#             return num1 * num2
#         elif operation == '/':
#             return num1 / num2
#         else:
#             print(f"Error: Unknown operation '{operation}'")
#             return None
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero")
#         return None
#     except TypeError:
#         print("Error: Invalid number types")
#         return None
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return None
# 
# print(calculator(10, 5, '+'))
# print(calculator(10, 0, '/'))
# print(calculator(10, "five", '+'))

"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. Functions:
   - Define with 'def function_name(parameters):'
   - Use 'return' to send back values
   - Type hints improve code clarity: -> return_type
   - Functions make code reusable and organized

2. Type Checking:
   - isinstance(value, type) checks variable types
   - Useful for validation before operations
   - Available types: int, str, float, bool, list, dict, tuple, etc.

3. Exception Handling:
   - try: code that might fail
   - except: code to run if error occurs
   - else: runs if NO error (optional)
   - finally: always runs (optional)

4. Exception Types:
   - ZeroDivisionError: division by zero
   - ValueError: wrong value type/format
   - TypeError: wrong data type
   - KeyError: dictionary key not found
   - Exception: catches all (use carefully!)

5. Best Practices:
   - Catch specific exceptions first
   - Don't hide errors silently
   - Use meaningful error messages
   - Validate inputs in functions
   - Use exceptions for unexpected errors only

Remember: Functions organize code, exceptions prevent crashes!
"""
