class Player():
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        return self
    
p1 = Player("mohamed", 19)

print(p1.run())
