class Player():
    membership= True #class obj attribute
    #the difference this one 🔼 is statique 
    #those 🔽 are dynamic
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        if (Player.membership):
            print(f"{self.name} running")
        else :
            print(f"{self.name} not running")
    def shout(self):
        print(f"my name is {self.name} , i'm {self.age} y.o")
        #cant use Player.age bcs its not a class obj attribute
        # its defined in our constructor fct __init__

p1 = Player("mohamed", 19)
p2 = Player("khalil", 20)
p1.attack = 50
p2.membership=False

print(p1.name)
print(p2.age)
print(f"Attack damage :{p1.attack}")
# help(Player)
#help(p1)
print(p1.membership)
print(p2.membership)
p1.run()
p2.run()
p1.shout()