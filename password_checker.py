import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Lowercase check
    if re.search("[a-z]", password):
        strength += 1

    # Uppercase check
    if re.search("[A-Z]", password):
        strength += 1

    # Number check
    if re.search("[0-9]", password):
        strength += 1

    # Special character check
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength result
    if strength <= 2:
        return "Weak Password ❌"
    elif strength == 3 or strength == 4:
        return "Medium Password ⚠️"
    else:
        return "Strong Password ✅"

# Input from user
password = input("Enter your password: ")
result = check_password_strength(password)

print("Password Strength:", result)