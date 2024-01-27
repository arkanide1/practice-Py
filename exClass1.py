# Given the below class:
class Cat():
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest(*cats):
    return max(*cats)


cat1 = Cat("Timmy", 4)
cat2 = Cat("Simba", 5)
cat3 = Cat("Tommy", 3)
print(f"the oldest cat is {oldest(cat1.age, cat2.age,cat3.age)} years old")



