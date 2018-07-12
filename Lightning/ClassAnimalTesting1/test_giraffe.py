import unittest
from giraffe import Giraffe


class Test_Giraffe(unittest.TestCase):
    def test_is_male(self):
        male_giraffe = Giraffe('male')
        self.assertTrue(male_giraffe.male)
        self.assertFalse(male_giraffe.female)

    def test_is_female(self):
        female_giraffe = Giraffe('female')
        self.assertTrue(female_giraffe.female)
        self.assertFalse(female_giraffe.male)

    def test_is_nonconforming_gender(self):
        nonconforming_giraffe = Giraffe('nonconforming')
        self.assertTrue(nonconforming_giraffe.female)
        self.assertFalse(nonconforming_giraffe.male)

    def test_eats_food(self):
        self.assertNotEqual(Giraffe().food, '')

    def test_habitat_is_savannah(self):
        self.assertEqual(Giraffe().habitat.lower(), 'savannah')

    def test_has_splotches(self):
        self.assertGreater(Giraffe().num_of_splotches, -1)

    def test_has_name(self):
        self.assertNotEqual(Giraffe().name, '')


if __name__ == '__main__':
    unittest.main()
