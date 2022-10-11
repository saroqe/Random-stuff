from extras import Payload
import sys
###And yet it still doesnt work (Tested it on Kali)
input("This could damage or destroy your computer, use at own risk. This virus can produce 1-10000 self-replicating files. Please undestand i am not responsible for any damages. Would you like to proceed in the execution? (Yes/n)")

if input == "Yes":
    Payload()
    
if input == "N" or "n" or "No":
    sys.exit()





