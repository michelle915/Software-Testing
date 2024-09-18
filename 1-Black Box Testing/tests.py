# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 7/10/2023
# Description: The following program implements unit tests

import unittest
from credit_card_validator import credit_card_validator
from random import randint, choice


class CreditCardTest(unittest.TestCase):

    def test_valid(self):
        # testing visa
        for _ in range(100):
            number = '4' + ''.join([str(randint(0, 9)) for _ in range(15)])
            self.assertTrue(credit_card_validator(number))

        # testing mastercard
        for _ in range(50):
            number = choice(['51', '52', '53', '54', '55']) + ''.join([str(randint(0, 9)) for _ in range(14)])
            self.assertTrue(credit_card_validator(number))
        for _ in range(50):
            number = str(randint(2221, 2720)) + ''.join([str(randint(0, 9)) for _ in range(12)])
            self.assertTrue(credit_card_validator(number))

        # testing amex
        for _ in range(100):
            number = choice(['34', '37']) + ''.join([str(randint(0, 9)) for _ in range(13)])
            self.assertTrue(credit_card_validator(number))

    def test_invalid(self):
        for _ in range(100):
            number = ''.join([str(randint(0, 9)) for _ in range(16)])
            while number.startswith(('4', '51', '52', '53', '54', '55', '34', '37')) or (
                    2221 <= int(number[:4]) <= 2720):
                number = ''.join([str(randint(0, 9)) for _ in range(16)])
            self.assertFalse(credit_card_validator(number))

    def test1(self):
        """
        Verifies that a null entry return false.

             length: 0

        Picked using category partition
        """
        self.assertFalse(credit_card_validator(""))

# GENERAL INVALID  PREFIXES

    def testPREFIX1(self):
        """
        Verifies that a card number with a length of 16 and a valid check digit returns false if it is
        not a Visa or Mastercard.

             issuer: ?
             prefix: Invalid (Visa: 4. MC: 51-55; 2221-2720)) -> 0
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("0000141234567891"))

    def testPREFIX2(self):
        """
        Verifies that a card number with a length of 16 and a valid check digit returns false if it is
        not a Visa or Mastercard.

             issuer: ?
             prefix: Invalid (Visa: 4. MC: 51-55; 2221-2720)) -> 1
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("1800141234567891"))

    def testPREFIX3(self):
        """
        Verifies that a card number with a length of 16 and a valid check digit returns false if it is
        not a Visa or Mastercard.

             issuer: ?
             prefix: Invalid (Visa: 4. MC: 51-55; 2221-2720)) -> 3
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("3400141234567891"))

    def testPREFIX4(self):
        """
        Verifies that a card number with a length of 16 and a valid check digit returns false if it is
        not a Visa or Mastercard.

             issuer: ?
             prefix: Invalid (Visa: 4. MC: 51-55; 2221-2720)) -> 6
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("6700141234567891"))

    def testPREFIX5(self):
        """
        Verifies that a card number with a length of 16 and a valid check digit returns false if it is
        not a Visa or Mastercard.

             issuer: ?
             prefix: Invalid (Visa: 4. MC: 51-55; 2221-2720)) -> 7
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("7500141234567891"))

    def testPREFIX6(self):
        """
        Verifies that a card number with a length of 16 and a valid check digit returns false if it is
        not a Visa or Mastercard.

             issuer: ?
             prefix: Invalid (Visa: 4. MC: 51-55; 2221-2720)) -> 8
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("8300141234567891"))

    def testPREFIX7(self):
        """
        Verifies that a card number with a length of 16 and a valid check digit returns false if it is
        not a Visa or Mastercard.

             issuer: ?
             prefix: Invalid (Visa: 4. MC: 51-55; 2221-2720)) -> 9
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("9100141234567891"))

    def testPREFIX8(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 0
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("020014123456789"))

    def testPREFIX9(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 1
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("160014123456789"))

    def testPREFIX10(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 2
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("210014123456789"))

    def testPREFIX11(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 4
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("400014123456789"))

    def testPREFIX12(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 5
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("590014123456789"))

    def testPREFIX13(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 6
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("640014123456789"))

    def testPREFIX14(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 7
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("780014123456789"))

    def testPREFIX15(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 8
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("830014123456789"))

    def testPREFIX16(self):
        """
        Verifies that a card number with a length of 15 and a valid check digit returns false if it is
        not an Amex.

             issuer: ?
             prefix: Invalid (34 & 37) -> 9
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("970014123456789"))

# 16 DIGITS - AMEX PREFIXES

    def testPREFIX17(self):
        """
        Verifies that a 16-digit number with an AMEX prefix returns false.

             issuer: Visa/MasterCard
             prefix: Invalid (AMEX: 34 & 37)
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("3461441635108147"))

    def testPREFIX18(self):
        """
        Verifies that a 16-digit number with an AMEX prefix and invalid check digit returns false.

             issuer: Visa/MasterCard
             prefix: Invalid (AMEX: 34 & 37)
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("3461441635108146"))

# 15 DIGITS - VISA/MASTERCARD PREFIXES

    def testPREFIX19(self):
        """
        Verifies that a 15-digit number with a VISA prefix and invalid check digit returns false.

             issuer: Amex
             prefix: Invalid (VISA:4)
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("461441635108143"))

    def testPREFIX20(self):
        """
        Verifies that a 16-digit number with a VISA prefix and invalid check digit returns false.

             issuer: Amex
             prefix: Invalid (VISA:4)
             length: Valid (15)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("461441635108149"))

    def testPREFIX21(self):
        """
        Verifies that a 15-digit number with a MasterCard prefix and invalid check digit returns false.

             issuer: Amex
             prefix: Invalid (MasterCard: 51-55; 2221-2720) 51
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("511441635108143"))

    def testPREFIX22(self):
        """
        Verifies that a 15-digit number with a MasterCard prefix and invalid check digit returns false.

             issuer: Amex
             prefix: Invalid (MasterCard: 51-55; 2221-2720) 2221
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("222141635108149"))

    def testPREFIX23(self):
        """
        Verifies that a 15-digit number with a MasterCard prefix and invalid check digit returns false.

             issuer: Amex
             prefix: Invalid (MasterCard: 51-55; 2221-2720)
             length: Valid (15)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("511441635108144"))

    def testPREFIX24(self):
        """
        Verifies that a 15-digit number with a MasterCard prefix and invalid check digit returns false.

             issuer: Amex
             prefix: Invalid (MasterCard: 51-55; 2221-2720)
             length: Valid (15)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("222141635108148"))

# VISA CHECKS - ALL VALID

    def testVISA1(self):
        """
        Verifies that a Visa number with a valid prefix, length, and check digit returns true.

             issuer: Visa
             prefix: Valid (4)
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertTrue(credit_card_validator("4611328157593581"))

# VISA CHECKS - INVALID CHECK DIGIT

    def testVISA2(self):
        """
        Verifies that a Visa number with a valid prefix and length but an incorrect check digit returns false.

             issuer: Visa
             prefix: Valid (4)
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("4703656177468872"))

# VISA CHECKS - INVALID LENGTH

    def testVISA3(self):
        """
        Verifies that a Visa number with a valid prefix and check digit but incorrect length (-1) returns false.

             issuer: Visa
             prefix: Valid (4)
             length: Invalid (16) -> 15
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("421234123412302"))

    def testVISA4(self):
        """
        Verifies that a Visa number with a valid prefix and check digit but incorrect length (+1) returns false.

             issuer: Visa
             prefix: Valid (4)
             length: Invalid (16) -> 17
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("42123412341230002"))

# VISA CHECKS - COMBINATION

    def testVISA5(self):
        """
        Verifies that a Visa number with a valid prefix but an invalid length
        and invalid check degit returns false.

             issuer: Visa
             prefix: Valid (4)
             length: Invalid (16) -> 17
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("40001111000011110"))

    def testVISA6(self):
        """
        Verifies that a Visa number with a valid prefix but an invalid length
        and invalid check degit returns false.

             issuer: Visa
             prefix: Valid (4)
             length: Invalid (16) -> 15
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("400011110000111"))

    def testVISA7(self):
        """
        Verifies that a Visa number with a valid length but an invalid prefix
        and invalid check degit returns false.

             issuer: Visa
             prefix: Invalid (4)
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("3000111100001111"))

    def testVISA8(self):
        """
        Verifies that a Visa number with a valid check digit but an invalid prefix
        and invalid length returns false.

             issuer: Visa
             prefix: Invalid (4) -> 9
             length: Invalid (16) -> 17
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("98858970648367192"))

    def testVISA9(self):
        """
        Verifies that a Visa number with a valid check digit but an invalid prefix
        and invalid length returns false.

             issuer: Visa
             prefix: Invalid (4) -> 9
             length: Invalid (16) -> 15
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("988589706483671"))

    def testVISA510(self):
        """
        Verifies that a Visa number with an invalid check digit, an invalid prefix
        and invalid length returns false.

             issuer: Visa
             prefix: Invalid (4) -> 9
             length: Invalid (16) -> 17
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("91110000111100001"))

    def testVISA511(self):
        """
        Verifies that a Visa number with an invalid check digit, an invalid prefix
        and invalid length returns false.

             issuer: Visa
             prefix: Invalid (4) -> 9
             length: Invalid (16) -> 15
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("911100001111001"))

# MASTERCARD CHECKS - ALL VALID

    def testMC1(self):
        """
        Verifies that a MasterCard number with a valid 51 prefix, length, and check digit returns true.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 51
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertTrue(credit_card_validator("5123593721117344"))

    def testMC2(self):
        """
        Verifies that a MasterCard number with a valid 55 prefix, length, and check digit returns true.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 55
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertTrue(credit_card_validator("5585888023071210"))

    def testMC3(self):
        """
        Verifies that a MasterCard number with a valid 2221 prefix, length, and check digit returns true.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 2221
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertTrue(credit_card_validator("2221835511172874"))

    def testMC4(self):
        """
        Verifies that a MasterCard number with a valid 2720 prefix, length, and check digit returns true.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 2720
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertTrue(credit_card_validator("2720822463109651"))

# MASTERCARD CHECKS - INVALID CHECK DIGIT

    def testMC5(self):
        """
        Verifies that a MasterCard number with a valid 51 prefix and length but an invalid check digit returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 51
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("5100000000000000"))

    def testMC6(self):
        """
        Verifies that a MasterCard number with a valid 55 prefix and length but an invalid check digit returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 55
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("5500000000000000"))

    def testMC7(self):
        """
        Verifies that a MasterCard number with a valid 2221 prefix and length but an invalid check digit returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 2221
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("2221000000000000"))

    def testMC8(self):
        """
        Verifies that a MasterCard number with a valid 2720 prefix and length but an invalid check digit returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 2720
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("2720000000000000"))

# MASTERCARD CHECKS - INVALID LENGTH

    def testMC9(self):
        """
        Verifies that a MasterCard number with a valid prefix and check digit but
        incorrect length (-1) returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720)
             length: InValid (16) -> 15
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("250112128232840"))

    def testMC10(self):
        """
        Verifies that a MasterCard number with a valid prefix and check digit but
        incorrect length (+1) returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720)
             length: InValid (16) -> 17
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("25804937142811379"))

# MASTERCARD CHECKS - INVALID PREFIX

    def testMC11(self):
        """
        Verifies that a MasterCard number with a valid check digit and length but
        invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 50
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("5012345678910005"))

    def testMC12(self):
        """
        Verifies that a MasterCard number with a valid check digit and length but
        invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 56
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("5612345678910009"))

    def testMC13(self):
        """
        Verifies that a MasterCard number with a valid check digit and length but
        invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 2220
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("2220345678910000"))

    def testMC14(self):
        """
        Verifies that a MasterCard number with a valid check digit and length but
        invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 2721
             length: Valid (16)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("2721345678910004"))

# MASTERCARD CHECKS - COMBINATION

    def testMC16(self):
        """
        Verifies that a MasterCard number with a valid prefix but an invalid length
        and invalid check degit returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 51
             length: Invalid (16) -> 17
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("51001111000011110"))

    def testMC17(self):
        """
        Verifies that a MasterCard number with a valid prefix but an invalid length
        and invalid check degit returns false.

             issuer: MasterCard
             prefix: Valid (51-55; 2221-2720) -> 51
             length: Invalid (16) -> 15
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("510011110000111"))

    def testMC18(self):
        """
        Verifies that a MasterCard number with a valid length but an invalid prefix
        and invalid check degit returns false.

             issuer: MasterCard
             prefix: InValid (51-55; 2221-2720) -> 56
             length: Valid (16)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("5600111100001111"))

    def testMC19(self):
        """
        Verifies that a MasterCard number with a valid check digit but an invalid length
        and invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 2220
             length: Invalid (16) -> 17
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("22201111222211118"))

    def testMC20(self):
        """
        Verifies that a MasterCard number with a valid check digit but an invalid length
        and invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 2721
             length: Invalid (16) -> 15
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("272111112222118"))

    def testMC21(self):
        """
        Verifies that a MasterCard number with a valid check digit but an invalid length
        and invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 50
             length: Invalid (16) -> 17
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("50112222111122221"))

    def testMC22(self):
        """
        Verifies that a MasterCard number with a valid check digit but an invalid length
        and invalid prefix returns false.

             issuer: MasterCard
             prefix: Invalid (51-55; 2221-2720) -> 2220
             length: Invalid (16) -> 15
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("222022221111222"))

# AMEX CHECKS - ALL VALID

    def testAMEX1(self):
        """
        Verifies that an Amex number with a valid 34 prefix, length, and check digit returns true.

             issuer: Amex
             prefix: Valid (34 & 37) -> 34
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertTrue(credit_card_validator("348583535231340"))

    def testAMEX2(self):
        """
        Verifies that an Amex number with a valid 37 prefix, length, and check digit returns true.

             issuer: Amex
             prefix: Valid (34 & 37) -> 37
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertTrue(credit_card_validator("377165834169928"))

# AMEX CHECKS - CHECK DIGIT INVALID

    def testAMEX3(self):
        """
        Verifies that an Amex number with a valid 34 prefix and length but an invalid check digit returns false.

             issuer: Amex
             prefix: Valid (34 & 37) -> 34
             length: Valid (15)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("340000000000000"))

    def testAMEX4(self):
        """
        Verifies that an Amex number with a valid 37 prefix and length but an invalid check digit returns false.

             issuer: Amex
             prefix: Valid (34 & 37) -> 37
             length: Valid (15)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("370000000000000"))

# AMEX CHECKS - INVALID LENGTH

    def testAMEX5(self):
        """
        Verifies that an Amex number with a valid prefix and check digit but incorrect length (-1) returns false.

             issuer: Amex
             prefix: Valid (34 & 37) -> 34
             length: Invalid (15) -> 14
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("34123412340002"))

    def testAMEX6(self):
        """
        Verifies that an Amex number with a valid prefix and check digit but incorrect length (+1) returns false.

             issuer: Visa
             prefix: Valid (34 & 37) -> 34
             length: Invalid (15) -> 16
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("3412341234120008"))

# AMEX CHECKS - INVALID PREFIX

    def testAMEX7(self):
        """
        Verifies that an Amex number with a valid check digit and length but
        invalid prefix returns false.

             issuer: Amex
             prefix: Invalid (34 & 37) -> 33
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("331234123400009"))

    def testAMEX8(self):
        """
        Verifies that an Amex number with a valid check digit and length but
        invalid prefix returns false.

             issuer: Visa
             prefix: Invalid (34 & 37) -> 38
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("381234123400008"))

    def testAMEX9(self):
        """
        Verifies that an Amex number with a valid check digit and length but
        invalid prefix returns false.

             issuer: Amex
             prefix: Invalid (34 & 37) -> 35
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("351234123400004"))

    def testAMEX10(self):
        """
        Verifies that an Amex number with a valid check digit and length but
        invalid prefix returns false.

             issuer: Visa
             prefix: Invalid (34 & 37) -> 36
             length: Valid (15)
        check digit: Valid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("361234123400002"))

# AMEX CHECKS - COMBINATION

    def testAMEX11(self):
        """
        Verifies that a AMEX number with a valid prefix but an invalid length
        and invalid check degit returns false.

             issuer: Amex
             prefix: Valid (34 & 37)
             length: Invalid (15) -> 14
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("34112222111122"))

    def testAMEX12(self):
        """
        Verifies that a AMEX number with a valid prefix but an invalid length
        and invalid check degit returns false.

             issuer: Amex
             prefix: Valid (34 & 37)
             length: Invalid (15) -> 16
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("3711222211112222"))

    def testAMEX13(self):
        """
        Verifies that a AMEX number with a valid length but an invalid prefix
        and invalid check degit returns false.

             issuer: Amex
             prefix: InValid (34 & 37)
             length: Valid (15)
        check digit: Invalid

        Picked using category partition.
        """
        self.assertFalse(credit_card_validator("331122221111222"))


if __name__ == '__main__':
    unittest.main()
