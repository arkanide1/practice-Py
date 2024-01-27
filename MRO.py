# Method Resolution Order

class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B,C):
    pass


print(D.num)
print(D.mro())


""" how this realation looks like 

      A
     ↗ ↖
    B    C
     ↖ ↗
      D

D has multiple inheritence
B and C have inheritence from A

MRO : is a rule that python follows to demermie when you run a method which want to run

"""
