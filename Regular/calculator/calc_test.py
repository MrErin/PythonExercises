import unittest
import calculator


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
        self.assertEqual(self.calculator.add(2, 7), 9)

        # Write test methods for subtract, multiply, divide


if __name__ == '__main__':
    unittest.main()
