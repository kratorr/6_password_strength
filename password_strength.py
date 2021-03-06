import sys
import getpass


def load_blacklist(filepath):
    with open(filepath, "r") as file:
        blacklist = file.read().splitlines()
    return blacklist


def check_upper_lower_case(password, score=2):
    if any(char.isupper() for char in password):
        if any(char.islower() for char in password):
            return score


def check_numerical_digits(password, score=2):
    if any(char.isdigit() for char in password):
        return score


def check_special_characters(password, score=2):
    if any(not char.isalnum() for char in password):
        return score


def check_password_lenght(password, score=2, min_password_lenght = 8):
    if len(password) > min_password_lenght:
        return score


def check_password_in_black_list(password, blacklist, score=2):
    if password not in blacklist:
        return score


if __name__ == "__main__":
    try:
        blacklist = load_blacklist(sys.argv[1])
    except FileNotFoundError:
        exit("File not found")
    password = getpass.getpass("Enter your password: ")
    check_list = [
        check_upper_lower_case(password),
        check_numerical_digits(password),
        check_special_characters(password),
        check_password_lenght(password),
        check_password_in_black_list(password, blacklist)
    ]
    password_strength = sum(filter(None, check_list))
    print("Your password strength (1-10): ", password_strength)
