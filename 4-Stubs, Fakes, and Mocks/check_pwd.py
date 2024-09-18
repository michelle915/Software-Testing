# Author: Michelle Loya
# Date: 7/30/2023
# Description: The following program implements a password validator program.
#
# Must be between 8 and 20 characters (inclusive)
# Must contain at least one lowercase letter (standard English alphabet)
# Must contain at least one uppercase letter (standard English alphabet)
# Must contain at least one digit
# Must contain at least one symbol from: ~`!@#$%^&*()_+-= (copy and paste
# to avoid missing characters) These are the only symbols that will meet
# this requirement. Other symbols may be present, but they won't satisfy this requirement.

def check_pwd(password):
    # no input
    if len(password) == 0:
        return False

    # too short
    if len(password) <= 7:
        return False

    # too long
    if len(password) > 20:
        return False

    # no lower case
    if not any(char.islower() for char in password):
        return False

    # no upper case
    if not any(char.isupper() for char in password):
        return False

    # no number
    if not any(char.isnumeric() for char in password):
        return False

    # no special symbol
    symbols = '~`!@#$%^&*()_+-='
    if not any(char in symbols for char in password):
        return False

    return True
