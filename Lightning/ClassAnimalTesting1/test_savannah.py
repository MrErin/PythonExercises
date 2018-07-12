import unittest
from savannahHabitat import Savannah


savannah = Savannah()

class habitatTest(unittest.TestCase):

    def test_savannah_is_habitat(self):
        self.assertEqual(savannah.my_name(), "Savannah")


if __name__ == '__main__':
    unittest.main()
