class Player():
    membership = True
    def __init__(self, name="anonymous", age=0):
        if (age>18):
            self.name = name
            self.age = age
    def shout(self):
        print(f"my name is {self.name}, i'm {self.age} y.o")

p1 = Player("mohamed")
p2 = Player("khalil", 20)

p1.shout()
