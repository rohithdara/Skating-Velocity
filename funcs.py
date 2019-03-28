#Project1
#
#Name: Rohith Dara
#Instructor: S. Einakian
#Section: 01

import math

#Convert pounds to kilograms
#float -> float
def poundsToKG(pounds):
   pounds = float(pounds)
   massSkater = pounds *0.453592
   return massSkater

#Take in the object's character and return the mass of the object in kg
#str -> float
def getMassObject(object):
   if object == 't':
      massObject = 0.1
      return massObject
   elif object == 'p':
      massObject = 1.0
      return massObject
   elif object == 'r':
      massObject = 3.0
      return massObject
   elif object == 'g':
      massObject = 5.3
      return massObject
   elif object == 'l':
      massObject = 9.07
      return massObject
   else:
      return 0.0
   
#Take in the distance and return the velocity of the object
#float -> float
def getVelocityObject(distance):
   velocityObject = math.sqrt((9.8*distance)/2)
   return velocityObject

#Take in the mass of the skater, mass of the object, and the velocity of the object and returns the velocity of the skater
#float float float -> float
def getVelocitySkater(massSkater,massObject,velocityObject):
   velocitySkater = (massObject*velocityObject)/massSkater
   return velocitySkater

