import unittest

from lootbag import Lootbag
from kid import Kid


class Test_Lootbag(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.red_bag = Lootbag('red')
        self.Amy = Kid('Amy', 1)
        self.Bruce = Kid('Bruce', 0)
        self.red_bag.kids.add(self.Amy)
        self.red_bag.kids.add(self.Bruce)
        self.Amy.add_toy('bike')
        self.Amy.add_toy('ball')
        self.Amy.add_toy('calculator')

    def test_lootbag_exists(self):
        self.assertIsInstance(self.red_bag, Lootbag)
        self.assertEqual(self.red_bag.color, 'red')
        self.assertNotEqual(self.red_bag.color, 'green')

    def test_lootbag_has_kids(self):
        self.assertEqual(len(self.red_bag.kids), 2)
        self.assertNotEqual(len(self.red_bag.kids), 0)

    def test_add_toy_to_kid(self):
        self.assertIn('bike', self.Amy.toys)
        self.assertNotIn('car', self.Amy.toys)

    def test_remove_toy_from_kid(self):
        self.Amy.add_toy('doll')
        self.assertIn('doll', self.Amy.toys)
        self.Amy.remove_toy('doll')
        self.assertNotIn('doll', self.Amy.toys)

    def test_delivery(self):
        self.Amy.delivered = False
        self.Amy.deliver_all_toys()
        self.assertTrue(self.Amy.delivered)


if __name__ == '__main__':
    unittest.main()
