#string concatenation
#from inspect import formatannotation
#youtuber = "Sam"
#print("subscribe to "+ youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

from email.mime import nonmultipart
from os import uname


adj = input("Adjective:")
noun = input ("Noun:")
verb = input("Verb:")
adverb = input("Adverb:")
noun1 = input("Noun:")
verb1 = input("Verb:")
noun2 = input("Noun:")
adverb1 = input("adverb:")
verb2 = input("Verb:")
madlib = f"Hey {noun}! Today is a very {adj} day.\
Lets go out and do some {verb} because it is very {adverb}.\
Sometimes {noun1} finds things are getting hard because of {noun}.\
{verb1} is a good activity for the betterment of there {noun2}.\
Well, this blows off heat and makes their {noun2} better because {adverb1}{verb2}.\
"
         
print(madlib)