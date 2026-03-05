# re stands for regular expressions.
# It allows you to: Match patterns,Split text based on patterns, Search text, ...
import re


def isStrongPassword(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    return re.match(pattern, password) is not None


def passwordValidator():
    password = input("Please enter your password:")

    if isStrongPassword(password):
        print("Strong password ✅")

    else:
        print("Password must contain:")
        print("- At least 8 characters")
        print("- Uppercase letter")
        print("- Lowercase letter")
        print("- Number")
        print("- Special character (@$!%*?&)")
        passwordValidator()


passwordValidator()
