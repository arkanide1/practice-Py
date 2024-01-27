# By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class.
from typing import Any


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
            'color':"Blue"
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return ('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]
    
    def __class__(self,i):
        return self.my_dict[i]
    def __delattr__(self):
        return f"delattr : {self.color}"
    def __module__(self):
        return "module"
    
action_figure = Toy('red', 0)
print(dir(action_figure))

print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
print(action_figure['has_pets'])

print(action_figure.__delattr__())
print(action_figure.__module__())

class SuperList(list):
    def __len__(self):
        return 1000

s= SuperList()
s.append(10)
s.append(2)
print(s)
print(issubclass(SuperList,object))
