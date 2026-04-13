def validate_ip_address(ip_string: str) -> bool:
    '''
    Validate IPv4 address format and range.
    Args:
        ip_string (str): IP address to validate    
    Returns:
        bool: True if valid, False otherwise
    Raises:
        ValueError: If IP format is invalid
    Example:
        validate_ip_address('192.168.1.1')
        True
        >>> validate_ip_address('999.999.999.999')
        False
    '''
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip_string):
        return False
    
    octets = ip_string.split('.')
    return all(0 <= int(octet) <= 255 for octet in octets)

validate_ip_address()

def foo(boo):
    '''
    This is a stupid func.
    Args:
        boo (str): arg to ret
    '''
    return boo

print('hello')

foo()