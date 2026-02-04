import re
import sys

def check_password_strength(password):
    """
    At least one special character
    At least 8 characters
    Includes uppercase letters
    Includes lowercase letters
    Includes numbers

    """
    length_ok = len(password) >= 8
    lowercase_ok = re.search(r'[a-z]', password)
    uppercase_ok = re.search(r'[A-Z]', password)
    digits_ok = re.search(r'\d', password)
    special_char_ok = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    feedback = []

    if not length_ok:
        feedback.append("Password must be at least 8 characters long")
    if not lowercase_ok:
        feedback.append("Password must contain at least one uppercase letter")
    if not uppercase_ok:
        feedback.append("Password must contain at least one uppercase letter")
    if not digits_ok:
        feedback.append("Password must contain at least one digit")
    if not special_char_ok:
        feedback.append("Password must contain at least one special character")

    if all([length_ok, lowercase_ok, uppercase_ok, digits_ok, special_char_ok]):
        return "Strong", []
    else:
        return "Weak", feedback



if __name__ == "__main__":

    while True:
        password = input("Enter a password to check its strength (or 'exit' to quit): ")
        if password.lower() == 'exit':
            sys.exit()

        strength, feedback = check_password_strength(password)
        print(f"\nPassword strength: {strength}")

        if feedback:
            print("Reasons for weakness")
            for feedback in feedback:
                print(f"- {feedback}")



        print("-" * 30)






