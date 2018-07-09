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
