import unittest
from calculator import Calculator


def setUpModule():
    # ? What is this for?
    # print('set up module')


def tearDownModule():
    # ? What is this for?
    # print('tear down module')


class Test_Calculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.my_calc = Calculator()

    # ? What is this for?
    @classmethod
    def tearDownClass(self):
        # print('tear down class')

    def test_is_instance(self):
        self.assertIsInstance(self.my_calc, Calculator)

    def test_add(self):
        self.assertEqual(self.my_calc.add(2, 7), 9)
        self.assertEqual(self.my_calc.add(-2, 7), 5)

    def test_subtract(self):
        self.assertEqual(self.my_calc.subtract(10, 5), 5)
        self.assertEqual(self.my_calc.subtract(10, -5), 15)

    def test_multiply(self):
        self.assertEqual(self.my_calc.multiply(2, 7), 14)
        self.assertEqual(self.my_calc.multiply(-2, 7), -14)

    def test_divide(self):
        self.assertEqual(self.my_calc.divide(8, 4), 2)
        self.assertEqual(self.my_calc.divide(8, -4), -2)


if __name__ == '__main__':
    unittest.main()
