import os



code = ("""
import os
        
with open("virus.py", "w") as f:
   f.write(code)    
       
os.system("python virus.py")
""")

with open("virus.py", "w") as f:
    f.write(code)
os.system("python virus.py")