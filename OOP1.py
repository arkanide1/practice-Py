# the 4 pillars of oop
# encapsulation:
# abstraction : means hidding of info and giving acess to what is necessary
# inheritance :
# polymorphism :

class User():
    def sign_in(self):
        print("logged in ")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"{self.name} attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"{self.name} attacking with {self.arrows} arrows")


# users : they can be wizards , arches
"""
the check all the users have access to we can use inheristance -> like that Wizard(User)
# an other thing python gives us a too to check if something is an inctance of a class
"""
wizard1 = Wizard("Merlin", "fire")
archer1 = Archer("Robin", 100)
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, object))

wizard1.attack()
archer1.attack()
"""
def playerAttack(char):
    char.attack()


for char in [wizard1,archer1]:
    char.attack()
"""
