#Imports
import os
import sys
import time
#Menu function
def menu():
    print("----PC Power Options----")
    time.sleep(1)


MenuChoice = input("""
    

1 - Shutdown
2 - Restart
3 - Cancel

   
""")

if MenuChoice == "1" or MenuChoice == "Shutdown":
    os.system('shutdown -s')

if MenuChoice == "2" or MenuChoice == "Restart":
    os.system('shutdown -r')

    if MenuChoice == "3" or MenuChoice == "Cancel":
        sys.exit()
   

