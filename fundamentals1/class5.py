class User(object):
    def __init__(self ,email):
        self.email= email
    def sign_in(self):
        print("logged in")
        if ():
            pass

class Wizard(User):
    def __init__(self, name , power, email):
        User.__init__(self, email)
        # another way of doing it 
        super().__init__(email)

        self.name = name 
        self.power = power

    def attack(self):
        print(f"{self.name} attaking with power of {self.power}")

wizard1= Wizard("Merlin", "fire", "merlin@gmail.com")
wizard1.sign_in()
wizard1.attack()
print(wizard1.email)

#introspection is the ability to determine the type of an obj at runtime
# python allows us to do introspection using "dir" fct 
# dir gives all the methods and attributes that the wizard instent has
#this is useful to see whaat use hae access to 

print(dir(wizard1))