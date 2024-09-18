# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 7/15/2023
# Description: The following program implements unit tests for a contrived_func method

import unittest
from contrived_func import contrived_func


class ContrivedFuncTest(unittest.TestCase):

    def test1(self):
        """
        ['a: F', 'b: T', 'c: T', 'd: T']  :  -2
        """
        contrived_func(-2)

    def test2(self):
        """
        ['a: F', 'b: F', 'c: T', 'd: T']  :  -1
        """
        contrived_func(-1)

    def test3(self):
        """
        ['a: F', 'b: T', 'c: T', 'd: F']  :  0
        """
        contrived_func(0)

    def test4(self):
        """
        ['a: F', 'b: F', 'c: T', 'd: F']  :  1
        """
        contrived_func(1)

    def test5(self):
        """
        ['a: T', 'b: T', 'c: T', 'd: F']  :  10
        """
        contrived_func(10)

    def test6(self):
        """
        ['a: T', 'b: F', 'c: T', 'd: F']  :  11
        """
        contrived_func(11)

    def test7(self):
        """
    ['a: T', 'b: T', 'c: F', 'd: F']  :  20
        """
        contrived_func(20)

    def test8(self):
        """
        ['a: T', 'b: F', 'c: F', 'd: F']  :  21
        """
        contrived_func(21)


if __name__ == '__main__':
    unittest.main()
