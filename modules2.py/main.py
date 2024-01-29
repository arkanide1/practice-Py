import sys
import random


min = int(sys.argv[1])
max = int(sys.argv[2])

rand = random.randint(min,max)

while(True):
    guess = int(input("enter a number :"))

    if ( guess < rand ):
        print(f"{guess} too low try again")
    elif (guess > rand):
        print(f"{guess} too high try again")
    elif (guess == rand):
        print("you nailed it")
        break




