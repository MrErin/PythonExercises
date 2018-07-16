import unittest

# this is supposed to make it possible to run tests from a different folder. It doesn't work for me. Still not sure why.
import sys
sys.path.append('../')

from animals import Animal
from animals import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog('Bob')

    def test_animal_exists(self):
        self.assertIsInstance(self.bob, Animal)
        self.assertIsInstance(self.bob, Dog)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    def test_animal_has_correct_name(self):
        self.bob.get_name()
        self.assertEqual(self.bob.name, 'Bob')

    def test_animal_has_correct_species(self):
        self.bob.set_species('C. lupus')
        self.assertEqual(self.bob.species.lower(), 'c. lupus')
        self.assertEqual(self.bob.get_species().lower(), 'c. lupus')

    def test_animal_returns_correct_str(self):
        self.assertEqual(self.bob.__str__().lower(), 'bob is a c. lupus')

    def test_dog_walks_at_speed(self):
        # creating a separate test class here because there is no "stop walking" method.
        self.bill = Dog('Bill')
        self.bill.set_legs(4)
        self.assertEqual(self.bill.speed, 0)
        self.bill.walk()
        self.assertEqual(
            self.bill.speed, (self.bill.speed + (0.2 * self.bill.legs)))


if __name__ == '__main__':
    unittest.main()
