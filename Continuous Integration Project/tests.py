import unittest
from task import conv_endian, conv_num, my_datetime


class TestTasks(unittest.TestCase):

    # conv_num function tests
    def test_valid_int(self):
        """Tests strings that represent integers"""
        self.assertEqual(conv_num('12345'), 12345)

    def test_valid_float_1(self):
        """Tests strings that represent negative float"""
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test_valid_float_2(self):
        """Tests strings that represent a float without whole numbers"""
        self.assertEqual(conv_num('.45'), 0.45)

    def test_valid_float_3(self):
        """Tests strings that represent a float without a decimal"""
        self.assertEqual(conv_num('12345.'), 12345.0)

    def test_valid_hex(self):
        """Tests strings that represent a valid hex"""
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_invalid_hex(self):
        """Tests strings that represent an invalid hex"""
        self.assertIsNone(conv_num('0xaZ4'))

    def test_invalid_int(self):
        """Tests strings that represent an invalid integer"""
        self.assertIsNone(conv_num('12345A'))

    def test_invalid_float(self):
        """Tests strings that represent an invalid float"""
        self.assertIsNone(conv_num('12.3.45'))

    # my_datetime function tests
    def test_1(self):
        """Tests input of 0"""
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_2(self):
        """Test random input 1"""
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_3(self):
        """Test random input 2"""
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test_4(self):
        """Tests random input 3"""
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    # conv_endian function tests
    def test_big_endian_default(self):
        """Tests numbers with big-endian conversion as default"""
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_big_endian_explicit(self):
        """Tests numbers with explicit big-endian conversion"""
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_negative_big_endian(self):
        """Tests negative numbers with big-endian conversion"""
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_little_endian(self):
        """Tests numbers with little-endian conversion"""
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_negative_little_endian(self):
        """Tests negative numbers with little-endian conversion"""
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_negative_little_endian_with_keywords(self):
        """Tests negative numbers with little-endian conversion using keyword arguments"""
        self.assertEqual(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test_invalid_endian(self):
        """Tests numbers with invalid endian values"""
        self.assertIsNone(conv_endian(num=-954786, endian='small'))

    def test_edge(self):
        """Tests numbers with invalid endian values"""
        self.assertEqual(conv_endian(num=0), '00')


if __name__ == '__main__':
    unittest.main()
