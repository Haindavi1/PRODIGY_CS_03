import re


def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = sum(
        [length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria])

    feedback = "Password strength assessment:\n"
    if criteria_met == 5:
        feedback += "Strong password! Well done."
    else:
        feedback += "Weak password. Consider the following improvements:\n"
        if not length_criteria:
            feedback += "- Make your password at least 8 characters long.\n"
        if not lowercase_criteria:
            feedback += "- Include at least one lowercase letter.\n"
        if not uppercase_criteria:
            feedback += "- Include at least one uppercase letter.\n"
        if not number_criteria:
            feedback += "- Include at least one number.\n"
        if not special_char_criteria:
            feedback += "- Include at least one special character (e.g., !@#$%^&*()).\n"

    return feedback


def main():
    while True:
        password = input("Enter a password to assess its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Exiting the program.")
            break

        feedback = assess_password_strength(password)
        print(feedback)


if __name__ == "__main__":
    main()
