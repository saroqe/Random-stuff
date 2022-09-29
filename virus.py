import os


### couldnt define the code var on line 9, will fix later
code = ("""
import os
        
with open("virus.py", "w") as f:
   f.write(code)    
       
os.system("python virus.py")
""")

with open("virus.py", "w") as f:
    f.write(code)
os.system("python virus.py")
