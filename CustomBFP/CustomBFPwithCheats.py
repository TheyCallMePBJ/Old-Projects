import itertools
import time

#These are multiple lists that will be chosen based on which complexity level is chosen
alpha_l = ("abcdefghijklmnopqrstuvwxyz")
alpha_u = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = ("1234567890")
SpecialChar = ("`~!@#$%^&*()_-+=|{}[],;:'.><?/" + '"\\')

#Defines the list of characters
Alphabet = alpha_l

#This sets the character set based on the user input
complexity = int(input("What complexity level would you like to choose? (1-4)\n"))
if complexity == 1:
    Alphabet = alpha_l
elif complexity == 2:
    Alphabet = alpha_l + alpha_u
elif complexity == 3:
    Alphabet = alpha_l + alpha_u + numbers
elif complexity == 4:
    Alphabet = alpha_l + alpha_u + numbers + SpecialChar

#This sets the start time so that it can be used later on in the program to calculate how long the program took.
start = time.time()

#This tells us how many combinations are used.
counter = 0

#This sets the character length of the password.
CharLength = 7

#This finds all of the possible combinations of characters that are of the correct length.
passwords = (itertools.product(Alphabet, repeat = CharLength))

#Outputs the number of characters in the set
print("\nThere are",len(list(Alphabet)),"characters in the set.\n")

#Counts the number of variations for a given set and character length
for i in passwords:
    counter = counter +1

#Gets the end time and subtracts the start time from it to calculate the time taken by the program
end = time.time()
timetaken = end - start

#Outputs the total number of variations tested and the time it took to do so
print(counter,"variations were tested.")
print("It took",timetaken,"seconds")
print(counter/timetaken,"iterations per second")