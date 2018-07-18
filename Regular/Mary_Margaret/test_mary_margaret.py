import unittest

from mary import Mary
from margaret import Margaret


class Test_Mary_Margaret(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.test_Mary = Mary()
        self.test_Margaret = Margaret()
        self.filepath = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "mary_margaret_file.txt")

    def test_Mary_exists(self):
        self.assertIsInstance(self.test_Mary, Mary)

    def test_Margaret_exists(self):
        self.assertIsInstance(self.test_Margaret, Margaret)

    def test_Margaret_talks(self):
        outfile


if __name__ == '__main__':
    unittest.main()
