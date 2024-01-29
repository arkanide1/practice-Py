from typing import Any


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 10
    def __del__(self):
        return "deleted!"
    def __call__(self):
        return "yeeess"
    


action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure.__len__())
print(len(action_figure))

print(action_figure.__del__())
print(action_figure.__call__())


# print(dir(action_figure))
