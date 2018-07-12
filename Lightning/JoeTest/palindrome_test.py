import unittest
from palindrome import *


class Palindrome_Test(unittest.TestCase):
    @unittest.skip('demonstrating skipping')
    def test_fun_returns_8(self):
        self.assertEqual(fun(8), 8)

    def test_is_palindrome(self):
        self.assertTrue(Palindrome().is_palindrome('mom'))
        # self.assertTrue(Palindrome().is_palindrome('Mom'))
        self.assertTrue(Palindrome().is_palindrome('131'))


if __name__ == '__main__':
    unittest.main()
