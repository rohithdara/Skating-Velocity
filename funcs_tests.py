# Project 1 
# 
# Name: Rohith Dara
# Instructor: S. Einakian 
# Section: 01

import unittest
from funcs import *

class TestCases(unittest.TestCase):
          
   def test_poundsToKG1(self):
      self.assertEqual(poundsToKG(17),7.711064)
      self.assertEqual(poundsToKG(25),11.3398)      

   def test_getMassObject1(self):
      self.assertEqual(getMassObject('p'),1.0)
      self.assertEqual(getMassObject('g'),5.3)
      self.assertEqual(getMassObject('z'),0.0)

   def test_getVelocityObject(self):
      self.assertAlmostEqual(getVelocityObject(15),8.57321409974)
      self.assertAlmostEqual(getVelocityObject(25),11.0679718106)

   def test_getVelocitySkater(self):
      self.assertAlmostEqual(getVelocitySkater(50,1.0,15),0.3)
      self.assertAlmostEqual(getVelocitySkater(30,3.0,17),1.7)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

