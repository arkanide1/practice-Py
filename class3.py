class Player:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"my name is {self.name}, i'm {self.age} y.o")
    
    @classmethod
    def adding_things(cls, num1,num2):
        #cls stands for class
        return cls("aissam" , num1+num2)
    """
    """
    @staticmethod
    def adding_things2(num1,num2):
        #cls stands for class
        return  num1+num2

p1 = Player("mohamed",19)
p2 = Player("khalil", 20)
p3 = Player.adding_things(2,3)

print(p3.age)
print(p3.name)
print(p3.adding_things2(1,3))