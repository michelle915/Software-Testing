# Author: Michelle Loya
# Date: 7/30/2023
# Description: The following program implements unit tests for a password validator program.
#
# Must be between 8 and 20 characters (inclusive)
# Must contain at least one lowercase letter (standard English alphabet)
# Must contain at least one uppercase letter (standard English alphabet)
# Must contain at least one digit
# Must contain at least one symbol from: ~`!@#$%^&*()_+-= (copy and paste
# to avoid missing characters) These are the only symbols that will meet
# this requirement. Other symbols may be present, but they won't satisfy this requirement.

import unittest
from check_pwd import check_pwd


class PasswordTest(unittest.TestCase):
    def test_empty(self):
        """Checks for an empty string"""
        self.assertFalse(check_pwd(""))

    def test_short(self):
        """Checks that a password has at least 8 characters."""
        self.assertFalse(check_pwd("1234567"))

    def test_long(self):
        """Checks that a password has no more than 20 characters"""
        self.assertFalse(check_pwd("012345678901234567890"))

    def test_lower(self):
        """Checks that a password has at least one lower case letter."""
        self.assertFalse(check_pwd("ABCD!@12"))

    def test_upper(self):
        """Checks that a password has at least one upper case letter"""
        self.assertFalse(check_pwd("abcd!@12"))

    def test_num(self):
        """Checks that a password has at least one digit"""
        self.assertFalse(check_pwd("abcd!@#$"))

    def test_symbol(self):
        """Checks that a password has at least one special character"""
        self.assertFalse(check_pwd("abcd1234"))


if __name__ == '__main__':
    unittest.main()
