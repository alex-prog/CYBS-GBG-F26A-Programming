"""
010 - Input Validation and Sanitization: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the Input Validation and Sanitization exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Validate user input to prevent security vulnerabilities
- Use try/except blocks for input validation
- Master regular expressions (regex) for pattern matching
- Sanitize input to prevent injection attacks
- Implement allowlist/whitelist validation
- Handle common validation scenarios (ports, IPs, emails, passwords)

"""

import re
import html  # For HTML escaping to prevent XSS


# ============================================================================
# PART 1: Basic Input Validation with Try/Except
# ============================================================================
# Always validate user input - never trust external data!
# Use try/except to handle conversion errors

print("=== PART 1: Port Number Validation ===\n")

def validate_port(port_input):
    """
    Validates a port number string.
    
    Rules:
    - Must be a number (integer)
    - Must be in valid range: 1-65535
    
    Raises:
        ValueError: If port is not a number or out of range
    
    Returns:
        int: The validated port number
    """
    # First, try to convert to integer
    try:
        port = int(port_input)
    except ValueError:
        raise ValueError('Port must be a number')
    
    # Check if port is in valid range
    if not (1 <= port <= 65535):
        raise ValueError('Port must be between 1 and 65535')
    
    return port


# Example usage with error handling
print("Testing port validation:")

# Test valid port
try:
    user_port = '8080'
    valid_port = validate_port(user_port)
    print(f'[PASS] Valid port: {valid_port}')
except ValueError as e:
    print(f'[FAIL] Invalid input: {e}')

# Test invalid port (out of range)
try:
    valid_port = validate_port('99999')
    print(f'[PASS] Valid port: {valid_port}')
except ValueError as e:
    print(f'[FAIL] Invalid input: {e}')

# Test invalid port (not a number)
try:
    valid_port = validate_port('abc')
    print(f'[PASS] Valid port: {valid_port}')
except ValueError as e:
    print(f'[FAIL] Invalid input: {e}')

print()


# ============================================================================
# PART 2: String Validation (Length and Content)
# ============================================================================
# Validate string length and content to prevent buffer overflows
# and ensure data integrity

print("=== PART 2: Password and Username Validation ===\n")

def validate_pass_length(password):
    """
    Validates password length.
    
    Rules:
    - Minimum 8 characters (security best practice)
    - Maximum 128 characters (prevent DoS attacks)
    """
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters')
    if len(password) > 128:
        raise ValueError('Password too long (max 128 characters)')
    return True


def validate_username(username):
    """
    Validates and sanitizes a username.
    
    Rules:
    - Cannot be empty or whitespace-only
    - Maximum 50 characters
    - Strips leading/trailing whitespace
    """
    # Check for empty or whitespace-only input
    if (not username) or len(username.strip()) == 0:
        raise ValueError('Username cannot be empty')
    
    # Check length
    if len(username) > 50:
        raise ValueError('Username too long (max 50 characters)')
    
    # Return sanitized version (trimmed)
    return username.strip()


# Test password validation
print("Password validation:")
try:
    validate_pass_length('abc123')
    print('[PASS] Password valid')
except ValueError as e:
    print(f'[FAIL] {e}')

try:
    validate_pass_length('SecurePassword123!')
    print('[PASS] Password valid')
except ValueError as e:
    print(f'[FAIL] {e}')

print()

# Test username validation
print("Username validation:")
try:
    clean_name = validate_username('  alice  ')
    print(f'[PASS] Valid username: "{clean_name}"')
except ValueError as e:
    print(f'[FAIL] {e}')

try:
    clean_name = validate_username('   ')
    print(f'[PASS] Valid username: "{clean_name}"')
except ValueError as e:
    print(f'[FAIL] {e}')

print()


# ============================================================================
# PART 3: Regular Expressions for Pattern Matching
# ============================================================================
# Regex is powerful for validating formats like IPs, emails, URLs
# Pattern: r'^...$' where ^ = start, $ = end of string

print("=== PART 3: IP Address Validation with Regex ===\n")

def validate_ip_address(ip):
    """
    Validates IPv4 address format.
    
    Pattern: xxx.xxx.xxx.xxx where xxx is 0-255
    
    Returns:
        str: The validated IP address
    """
    # Simple IPv4 pattern: digits.digits.digits.digits
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    if not re.match(pattern, ip):
        raise ValueError('Invalid IP address format')
    
    # Check each octet is 0-255
    octets = ip.split('.')
    for octet in octets:
        if int(octet) > 255:
            raise ValueError('IP address octets must be 0-255')
    
    return ip


def validate_ip_advanced(ip):
    """
    Advanced IPv4 validation using precise regex.
    
    Pattern breakdown:
    - 25[0-5]: 250-255
    - 2[0-4][0-9]: 200-249
    - [01]?[0-9][0-9]?: 0-199
    """
    # More robust IPv4 pattern (validates ranges in one regex)
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    
    if not re.match(pattern, ip):
        raise ValueError('Invalid IP address format')
    
    return ip


# Test IP validation
print("IP address validation:")

test_ips = [
    '192.168.1.1',      # Valid
    '10.0.0.255',       # Valid
    '256.1.1.1',        # Invalid (256 > 255)
    '192.168.1',        # Invalid (missing octet)
    '192.168.1.1.1',    # Invalid (too many octets)
]

for ip in test_ips:
    try:
        valid_ip = validate_ip_address(ip)
        print(f'[PASS] Valid IP: {valid_ip}')
    except ValueError as e:
        print(f'[FAIL] {ip}: {e}')

print()


# ============================================================================
# PART 4: Email Validation
# ============================================================================
# Email format: username@domain.tld
# Note: Full email validation is complex; this is a basic version

print("=== PART 4: Email Validation ===\n")

def validate_email(email):
    """
    Validates email address format.
    
    Pattern:
    - Local part: letters, digits, dots, hyphens, underscores, +, %
    - @ symbol
    - Domain: letters, digits, dots, hyphens
    - TLD: at least 2 letters
    
    Returns:
        str: The validated email (lowercase)
    """
    # Basic email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        raise ValueError('Invalid email format')
    
    # RFC 5321 limit
    if len(email) > 254:
        raise ValueError('Email address too long')
    
    # Return lowercase version (emails are case-insensitive)
    return email.lower()


# Test email validation
print("Email validation:")

test_emails = [
    'user@example.com',           # Valid
    'alice.bob@company.co.uk',    # Valid
    'test+tag@domain.org',        # Valid
    'invalid.email',              # Invalid (no @)
    '@nodomain.com',              # Invalid (no local part)
    'noat.com',                   # Invalid (no @)
]

for email in test_emails:
    try:
        valid_email = validate_email(email)
        print(f'[PASS] Valid email: {valid_email}')
    except ValueError as e:
        print(f'[FAIL] {email}: {e}')

print()


# ============================================================================
# PART 5: Input Sanitization
# ============================================================================
# Sanitization: Clean input to remove/escape dangerous characters
# Different from validation: changes the input rather than rejecting it

print("=== PART 5: Input Sanitization ===\n")

def sanitize_filename(filename):
    """
    Sanitize a filename to prevent directory traversal attacks.
    
    Removes:
    - Path separators (/, \)
    - Special characters (<>:"|?*)
    - Leading/trailing dots and spaces
    
    Returns:
        str: Safe filename
    """
    # Characters that are dangerous in filenames
    dangerous_chars = '<>:"/\\|?*'
    
    # Replace each dangerous character with underscore
    for char in dangerous_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing dots and spaces
    # (prevents hidden files and path issues)
    filename = filename.strip('. ')
    
    # Prevent empty filenames
    if not filename:
        filename = 'unnamed_file'
    
    return filename


def sanitize_comment(comment_text):
    """
    Sanitize user comment to prevent XSS attacks.
    
    Steps:
    - Trim whitespace
    - Escape HTML entities (<, >, &, ", ')
    - Limit length to prevent DoS
    
    Returns:
        str: Safe comment text
    """
    # Remove leading/trailing whitespace
    comment_text = comment_text.strip()
    
    # Escape HTML entities to prevent XSS (Cross-Site Scripting)
    # Converts: < to &lt;, > to &gt;, etc.
    comment_text = html.escape(comment_text)
    
    # Limit length to prevent storage/display issues
    if len(comment_text) > 1000:
        comment_text = comment_text[:1000] + '...[truncated]'
    
    return comment_text


# Test filename sanitization
print("Filename sanitization:")
dangerous_files = [
    '../../etc/passwd',
    'my<file>.txt',
    'report|data.pdf',
    '...secrets...',
    '  document.doc  ',
]

for filename in dangerous_files:
    safe = sanitize_filename(filename)
    print(f'"{filename}" → "{safe}"')

print()

# Test comment sanitization
print("Comment sanitization:")
dangerous_comments = [
    '<script>alert("XSS")</script>',
    'Normal comment here',
    '<b>Bold text</b> attempt',
]

for comment in dangerous_comments:
    safe = sanitize_comment(comment)
    print(f'"{comment}" → "{safe}"')

print()


# ============================================================================
# PART 6: Allowlist/Whitelist Validation
# ============================================================================
# Allowlist: Only permit values from a predefined list
# This is the most secure validation method when possible

print("=== PART 6: Allowlist Validation ===\n")

def validate_security_level(level):
    """
    Validates security level using an allowlist approach.
    
    Only specific values are permitted.
    This prevents injection of unexpected values.
    
    Returns:
        str: Validated security level (lowercase)
    """
    # Define allowed values
    allowed_levels = ['low', 'medium', 'high', 'critical']
    
    # Check if input is in the allowlist
    if level.lower() not in allowed_levels:
        raise ValueError(f'Invalid security level. Must be one of: {", ".join(allowed_levels)}')
    
    return level.lower()


# Test allowlist validation
print("Security level validation:")
test_levels = ['low', 'HIGH', 'critical', 'extreme', 'Medium']

for level in test_levels:
    try:
        valid_level = validate_security_level(level)
        print(f'[PASS] Valid level: {valid_level}')
    except ValueError as e:
        print(f'[FAIL] {level}: {e}')

print()


# ============================================================================
# PART 7: Comprehensive Input Validation Example
# ============================================================================
# Real-world example: Validate all fields for a user registration

print("=== PART 7: User Registration Validation ===\n")

def validate_user_registration(username, email, password, role):
    """
    Comprehensive validation for user registration.
    
    Returns:
        dict: Validated and sanitized user data
    
    Raises:
        ValueError: If any validation fails
    """
    errors = []
    
    # Validate username
    try:
        clean_username = validate_username(username)
    except ValueError as e:
        errors.append(f"Username: {e}")
        clean_username = None
    
    # Validate email
    try:
        clean_email = validate_email(email)
    except ValueError as e:
        errors.append(f"Email: {e}")
        clean_email = None
    
    # Validate password
    try:
        validate_pass_length(password)
        clean_password = password  # In real app, would hash this!
    except ValueError as e:
        errors.append(f"Password: {e}")
        clean_password = None
    
    # Validate role (allowlist)
    try:
        clean_role = validate_security_level(role)
    except ValueError as e:
        errors.append(f"Role: {e}")
        clean_role = None
    
    # If there are errors, raise them all
    if errors:
        raise ValueError("Validation errors:\n" + "\n".join(f"  - {err}" for err in errors))
    
    # Return validated data
    return {
        'username': clean_username,
        'email': clean_email,
        'password': clean_password,
        'role': clean_role
    }


# Test user registration
print("User registration test 1 (valid):")
try:
    user_data = validate_user_registration(
        username='alice',
        email='alice@company.com',
        password='SecurePass123!',
        role='medium'
    )
    print('[PASS] Registration successful!')
    print(f'  Username: {user_data["username"]}')
    print(f'  Email: {user_data["email"]}')
    print(f'  Role: {user_data["role"]}')
except ValueError as e:
    print(f'[FAIL] Registration failed:\n{e}')

print()

print("User registration test 2 (multiple errors):")
try:
    user_data = validate_user_registration(
        username='',
        email='invalid-email',
        password='short',
        role='admin'
    )
    print('[PASS] Registration successful!')
except ValueError as e:
    print(f'[FAIL] Registration failed:\n{e}')

print()
print("=== Module Complete ===")


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: MAC Address Validator
Create a function to validate MAC addresses (format: XX:XX:XX:XX:XX:XX).

# def validate_mac_address(mac):
#     # MAC format: 6 groups of 2 hexadecimal digits, separated by colons
#     pattern = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
#     
#     if not re.match(pattern, mac):
#         raise ValueError('Invalid MAC address format')
#     
#     return mac.upper()  # Return in uppercase
# 
# # Test
# try:
#     mac = validate_mac_address('00:1A:2B:3C:4D:5E')
#     print(f'Valid MAC: {mac}')
# except ValueError as e:
#     print(e)


Exercise 2: Credit Card Sanitizer
Create a function that masks credit card numbers (show only last 4 digits).

# def mask_credit_card(card_number):
#     # Remove spaces and dashes
#     card_clean = card_number.replace(' ', '').replace('-', '')
#     
#     # Validate it's all digits and correct length
#     if not card_clean.isdigit():
#         raise ValueError('Card number must contain only digits')
#     
#     if len(card_clean) not in [13, 15, 16]:  # Common card lengths
#         raise ValueError('Invalid card number length')
#     
#     # Mask all but last 4 digits
#     masked = '*' * (len(card_clean) - 4) + card_clean[-4:]
#     
#     return masked
# 
# # Test
# print(mask_credit_card('1234-5678-9012-3456'))  # ************3456
# print(mask_credit_card('4532 1488 0343 6467'))  # ************6467



Exercise 3: URL Validator
Validate URLs with http:// or https:// protocol.

# def validate_url(url):
#     # Basic URL pattern
#     pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
#     
#     if not re.match(pattern, url):
#         raise ValueError('Invalid URL format (must start with http:// or https://)')
#     
#     # Length check
#     if len(url) > 2048:  # Common max URL length
#         raise ValueError('URL too long')
#     
#     return url
# 
# # Test
# test_urls = [
#     'https://example.com',
#     'http://site.org/page',
#     'ftp://invalid.com',
#     'not-a-url',
# ]
# 
# for url in test_urls:
#     try:
#         print(f'[PASS] Valid: {validate_url(url)}')
#     except ValueError as e:
#         print(f'[FAIL] {url}: {e}')


Exercise 4: Strong Password Validator
Create a comprehensive password validator with multiple rules.

# def validate_strong_password(password):
#     errors = []
#     
#     # Check length
#     if len(password) < 12:
#         errors.append('Password must be at least 12 characters')
#     
#     # Check for uppercase letter
#     if not re.search(r'[A-Z]', password):
#         errors.append('Password must contain at least one uppercase letter')
#     
#     # Check for lowercase letter
#     if not re.search(r'[a-z]', password):
#         errors.append('Password must contain at least one lowercase letter')
#     
#     # Check for digit
#     if not re.search(r'\d', password):
#         errors.append('Password must contain at least one digit')
#     
#     # Check for special character
#     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
#         errors.append('Password must contain at least one special character')
#     
#     # Check for common passwords (basic example)
#     common_passwords = ['Password123!', 'Admin123!', 'Welcome123!']
#     if password in common_passwords:
#         errors.append('Password is too common')
#     
#     if errors:
#         raise ValueError('\n'.join(errors))
#     
#     return True
# 
# # Test
# try:
#     validate_strong_password('Str0ng!P@ssw0rd')
#     print('[PASS] Password is strong')
# except ValueError as e:
#     print(f'[FAIL] Password validation failed:\n{e}')


Challenge 1: Input Validation Framework
Create a reusable validation framework with multiple validators.

# class ValidationRule:
#     def __init__(self, name, validator_func, error_msg):
#         self.name = name
#         self.validator_func = validator_func
#         self.error_msg = error_msg
#     
#     def validate(self, value):
#         if not self.validator_func(value):
#             raise ValueError(self.error_msg)
#         return True
# 
# class InputValidator:
#     def __init__(self):
#         self.rules = []
#     
#     def add_rule(self, rule):
#         self.rules.append(rule)
#     
#     def validate(self, value):
#         errors = []
#         for rule in self.rules:
#             try:
#                 rule.validate(value)
#             except ValueError as e:
#                 errors.append(str(e))
#         
#         if errors:
#             raise ValueError('\n'.join(errors))
#         
#         return True
# 
# # Usage example
# username_validator = InputValidator()
# username_validator.add_rule(
#     ValidationRule('length', lambda x: 3 <= len(x) <= 20, 'Username must be 3-20 characters')
# )
# username_validator.add_rule(
#     ValidationRule('alphanumeric', lambda x: x.isalnum(), 'Username must be alphanumeric')
# )
# username_validator.add_rule(
#     ValidationRule('no_numbers_start', lambda x: not x[0].isdigit(), 'Username cannot start with a number')
# )
# 
# try:
#     username_validator.validate('alice123')
#     print('[PASS] Username valid')
# except ValueError as e:
#     print(f'[FAIL] Validation failed:\n{e}')



"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. Input Validation Principles:
   - NEVER trust user input - always validate
   - Fail securely: reject invalid input, don't try to fix it
   - Validate on server side (client-side validation can be bypassed)
   - Use allowlists (whitelist) when possible - more secure than denylists
   - Validate both format AND content (type, length, range, pattern)

2. Common Validation Techniques:
   - Type conversion with try/except (int(), float(), etc.)
   - Length checking (min/max bounds)
   - Range checking (1 <= port <= 65535)
   - Regular expressions for pattern matching
   - Allowlist comparison for specific values

3. Regular Expression Patterns:
   - r'^...$' ensures full string match (^ = start, $ = end)
   - \d = digit, \w = word character, \. = literal dot
   - {m,n} = repeat m to n times, + = 1 or more, * = 0 or more
   - [a-zA-Z] = character class, [^...] = negated class
   - () = capture group, | = OR operator

4. Sanitization vs Validation:
   - Validation: Check if input is acceptable (reject if not)
   - Sanitization: Clean/modify input to make it safe (transform)
   - Both are important for security defense-in-depth
   - Common sanitization: html.escape(), strip(), replace()

5. Real-World Security Applications:
   - SQL injection prevention: Sanitize or use parameterized queries
   - XSS prevention: Escape HTML entities in user content
   - Path traversal prevention: Sanitize filenames (remove ../, /, \)
   - Email validation: Prevent header injection
   - Command injection: Never pass unsanitized input to system commands

6. Best Practices:
   - Collect all validation errors, don't stop at first one
   - Use descriptive error messages (helps legitimate users)
   - Log validation failures (may indicate attack attempts)
   - Keep validation logic in reusable functions
   - Document validation rules clearly
   - Test edge cases (empty strings, very long input, special characters)

7. Common Validation Patterns:
   - IPv4: r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
   - Email: r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
   - URL: r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
   - MAC: r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
   - Port: 1 <= port <= 65535
   - Password: len >= 8, various character requirements

Remember: Input validation is your first line of defense against many attacks!
Security is about layers - validate early, validate often, and never trust external data.
"""

