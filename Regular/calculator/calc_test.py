import unittest
from calculator import Calculator


def set_up_module():
    print('set up module')


def tear_down_module():
    print('tear down module')


class Test_Calculator(unittest.TestCase):

    @classmethod
    def set_up_class(self):
        print('set up class')
        # Create an instance of the calculator that can be used in all tests

    @classmethod
    def tear_down_class(self):
        print('Tear down class')

    def test_add(self):
        self.assertEqual(Calculator().add(2, 7), 9)

    def test_subtract(self):
        self.assertEqual(Calculator().subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(Calculator().multiply(2, 7), 14)

    def test_divide(self):
        self.assertEqual(Calculator().divide(8, 4), 2)

        # Write test methods for subtract, multiply, divide


if __name__ == '__main__':
    unittest.main()
