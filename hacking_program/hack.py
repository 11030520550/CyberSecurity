import re
import sys


def check_password_strength(password):
    """
    Analyzes password strength based on standard criteria and provides feedback.
    A strong password should have:
    - At least 8 characters long
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one special character
    """
    # Criteria flags
    length_ok = len(password) >= 8
    lowercase_ok = re.search(r'[a-z]', password) is not None
    uppercase_ok = re.search(r'[A-Z]', password) is not None
    digit_ok = re.search(r'\d', password) is not None
    # Special characters can be defined explicitly or using \W (non-alphanumeric)
    special_char_ok = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Collect feedback
    feedback = []
    if not length_ok:
        feedback.append("Password must be at least 8 characters long.")
    if not lowercase_ok:
        feedback.append("Password must contain at least one lowercase letter.")
    if not uppercase_ok:
        feedback.append("Password must contain at least one uppercase letter.")
    if not digit_ok:
        feedback.append("Password must contain at least one digit.")
    if not special_char_ok:
        feedback.append("Password must contain at least one special character.")

    # Determine overall strength
    if all([length_ok, lowercase_ok, uppercase_ok, digit_ok, special_char_ok]):
        return "Strong", []
    else:
        return "Weak", feedback


# User input and testing
if __name__ == "__main__":
    while True:
        password = input("Enter a password to check its strength (or 'exit' to quit): ")
        if password.lower() == 'exit':
            sys.exit()

        strength, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Reasons for weakness:")
            for item in feedback:
                print(f"- {item}")
        print("-" * 30)
