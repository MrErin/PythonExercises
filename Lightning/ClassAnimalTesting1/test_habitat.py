import unittest
from habitat import Habitat

try:
    test_habitat = Habitat()

except NameError:
    test_habitat = False

class Habitat_test(unittest.TestCase):
  def test_habitat_is_defined(self):
    """ 
    See if the object has been created
    """
    self.assertTrue(test_habitat)
    """ 
    See if created object is an instance of Habitat
    """
    self.assertIsInstance(test_habitat, Habitat)

  
if __name__ == '__main__':
    unittest.main()
