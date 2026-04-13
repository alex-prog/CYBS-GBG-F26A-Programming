#16-Mar-2026

# Validate port
def validate_port(port_input):
    try:
        port = int(port_input)
    except ValueError:
        raise ValueError('Port must be a number')
    
    if not (1 <= port <= 65535):
        raise ValueError('Port must be between 1 and 65535')
    
    return port

# Usage
try:
    user_port = input('Enter port number: ')
    valid_port = validate_port(user_port)
    print(f'Valid port: {valid_port}')
except ValueError as e:
    print(f'Invalid input: {e}')


# ------------------------------------------------------------
# Date: 23-Mar-2026

def validate_pass_length(password):
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters')
    if len(password) > 128:
        raise ValueError('Password too long (max 128 characters)')
    return True

def validate_username(username):
    if (not username) or len(username.strip()) == 0:
        raise ValueError('Username cannot be empty')
    if len(username) > 50:
        raise ValueError('Username too long (max 50 characters)')
    return username.strip()


import html
import re 
 
# def validate_ip_address(ip):
#     # Simple IPv4 pattern
#     pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
#     if not re.match(pattern, ip):
#         raise ValueError('Invalid IP address format')
    
#     return ip

def validate_ip_address(ip):
    # Simple IPv4 pattern
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
    # More robust IPv4 pattern
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if not re.match(pattern, ip):
        raise ValueError('Invalid IP address format')
    return ip

def validate_email(email):
    # Basic email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        raise ValueError('Invalid email format')
    
    if len(email) > 254:  # RFC 5321 limit (https://datatracker.ietf.org/doc/rfc5321/)
        raise ValueError('Email address too long')
    
    return email.lower()

# -- Sanitization example --
def sanitize_filename(filename):
    # Remove dangerous characters
    dangerous_chars = '<>:"/\\|?*'
    for char in dangerous_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing dots and spaces
    filename = filename.strip('. ')
    
    return filename

def sanitize_comment(comment_text):
    # Remove whitespace characters
    comment_text = comment_text.strip()
    
    # Escape HTML entities to prevent XSS
    comment_text = html.escape(comment_text)
    
    # Limit length
    if len(comment_text) > 1000:
        comment_text = comment_text[:1000] + '...[truncated]'

    return comment_text


def validate_security_level(level):
    # Only allow specific values
    allowed_levels = ['low', 'medium', 'high', 'critical']
    
    if level.lower() not in allowed_levels:
        raise ValueError(f'Invalid security level. Must be one of: {allowed_levels}')
    
    return level.lower()
