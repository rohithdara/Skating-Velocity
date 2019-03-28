#Project 1
#
#Name: Rohith Dara
#Professor: S. Einakian
#Section: 01

import funcs

#input the weight of a skater, an object, and distance from another skater and output the backward velocity of the thrower
#none -> none 
def main():
   pounds = float(input("How much do you weigh (pounds)? "))
   distance = float(input("How far away is your professor (meters)? "))
   object = input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")   

   massSkater = float(funcs.poundsToKG(pounds))
   massObject = float(funcs.getMassObject(object))
   velocityObject = float(funcs.getVelocityObject(distance))
   velocitySkater = float(funcs.getVelocitySkater(massSkater,massObject,velocityObject))
   velocitySkater = round(velocitySkater,3)
   
   print()

   if massObject <= 0.1:
      print("Nice throw!","You're going to get an F!")
   elif 0.1 < massObject <= 1.0:
      print("Nice throw!","Make sure your professor is OK.")
   elif massObject > 1.0:
      if distance < 20:
         print("Nice throw!","How far away is the hospital?")
      elif distance >= 20:
         print("Nice throw!","RIP professor.")
   print("Velocity of skater:",format(velocitySkater,".3f"),"m/s")
   if velocitySkater < 0.2:
      print("My grandmother skates faster than you!")
   if velocitySkater >= 1.0:
      print ("Look out for that railing!!!")

if __name__=='__main__':
   main()
