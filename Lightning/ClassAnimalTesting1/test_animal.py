import unittest
from animal import Animal

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class AnimalTest(unittest.TestCase):


    def test_does_animal_speak(self):
        animal = Animal()
        self.assertTrue(animal.say_something())
  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
