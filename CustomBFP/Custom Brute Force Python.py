#All of the functions we need come automatically with python but do need to be imported.
import itertools
import time

#This is basically a list of all the different characters that will be tried.
#You will notice many symbols missing as they were slowing down efficiency and very unlikely to appear.
Alphabet = ("abcdefghijklmnopqrstuvwxyz")

#This sets the start time so that it can be used later on in the program to calculate how long the program took.
start = time.time()

#This tells us how many combinations are used.
counter = 0

#This sets the length of the password
CharLength = 7

#This finds all of the possible combinations of characters that are of the correct length.
passwords = (itertools.product(Alphabet, repeat = CharLength))

for i in passwords:
    counter = counter + 1
end = time.time()
timetaken = end - start
print (timetaken)
print (counter)