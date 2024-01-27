class User():
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name , power):
        self.name = name 
        self.power = power

    def attack(self):
        print(f"{self.name} attaking with power of {self.power}")

class Archer(User):
    def __init__(self, name , arrows):
        self.name = name 
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining")
    def run(self):
        return "is running"

class Hank(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

h1= Hank("Bor", "fire", 100)
print(h1.run())
print(h1.check_arrows())
print(h1.attack())
print(h1.sign_in())