import random 

def flipcoin():
    return random.choice(["heads","tails"])


for i in range(10):
    print(flipcoin())