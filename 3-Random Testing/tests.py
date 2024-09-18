# Author: Michelle Loya
# Date: 7/23/2023
# Description: The following program implements unit tests for a credit card number validator program.

import unittest
from credit_card_validator import credit_card_validator
from random import randint, choice


class CreditCardTest(unittest.TestCase):

    def test(self):
        valid_lengths = [15, 16]

        for _ in range(0, 750000):
            odds = randint(0, 10)

            if odds == 0:
                credit_card = ''.join([str(randint(0, 9)) for _ in range(14)])
                credit_card_validator(credit_card)
            elif odds == 10:
                credit_card = ''.join([str(randint(0, 9)) for _ in range(17)])
                credit_card_validator(credit_card)
            else:
                credit_card = ''.join([str(randint(0, 9)) for _ in range(choice(valid_lengths))])
                credit_card_validator(credit_card)


if __name__ == '__main__':
    unittest.main()
