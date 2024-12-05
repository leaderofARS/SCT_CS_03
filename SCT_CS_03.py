import re

# List of common passwords to check against
common_passwords = [
    '123456', 'password', '123456789', '12345', '1234', 'qwerty', 'abc123', 
    'password1', 'letmein', 'welcome', 'admin', 'iloveyou', 'sunshine', 'welcome123'
]

# List of common dictionary words (expand as needed)
common_words = ['password', 'admin', 'user', 'letmein', 'qwerty', 'iloveyou', '12345']

def check_password_strength(password):
    strength = 0

    # Check password length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    
    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Check for digit
    if re.search(r'\d', password):
        strength += 1
    
    # Check for special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    
    # Check for repeated characters (more than 2 repeating chars)
    if re.search(r'(.)\1{2,}', password):
        strength -= 1  # Penalize if there are repeated characters
    
    # Check for common passwords
    if password.lower() in common_passwords:
        strength -= 1  # Penalize if it's a common password
    
    # Check for common words (like 'admin', 'user', 'password')
    if any(word in password.lower() for word in common_words):
        strength -= 1  # Penalize for common words
    
    # Check for sequential characters or keyboard patterns
    if re.search(r'123|abc|qwerty|asdf', password.lower()):
        strength -= 1  # Penalize for sequential characters
    
    # Password strength evaluation
    if strength >= 7:
        return "Strong password!"
    elif strength == 6:
        return "Good password!"
    elif strength >= 4:
        return "Fair password."
    else:
        return "Weak password."

# Sample usage
password = input("Enter your password: ")
print(check_password_strength(password))
