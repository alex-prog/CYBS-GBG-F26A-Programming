def check_password_strength(password):
    if len(password) < 12:
        return False
    
    isspecial, islower, isupper, isdigit = False, False, False, False
    
    for c in password:
        if c.isupper():
            isupper=True
        if c.islower():
            islower=True
        if c.isdigit():
            isdigit=True
        if c in '!@#$%^&*()':
            isspecial=True
    return isupper and islower and isdigit and isspecial
