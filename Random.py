#Initial imports
import datetime
import random
from secrets import choice
import docx



#Defining usename, saying hello
usename = input("What is ur name?????? ")

print("Hello there,", usename,",I will say yes or no depending on random.")


#Initial randomiser
responsesRand=["Yes", "No", "Sometimes"]


question = input("Question here:")

print(random.choice(responsesRand))

print("Were you offended by it? i so hope not..")
feedback = input("I was...:")

print("Created and wrote current data to RanDataLog.docx")

##Log to RanDataLog.docx (Optional, delete if dont want)##
with open("RanDataLog.docx", "w") as f:
    f.write(usename)
    f.write(question)
    f.write(feedback)
    

