import utility
# import outils.more_outils.item
from outils.more_outils.item import buy
from utility import multiply, divide


import random 
# dir shows all the methods of its parameter
#print(dir(random))

# this is another way of doing it but its not recommended
# from outils.more_outils import *

# print(utility.multiply(3,4))

# print(outils.more_outils.item.buy("course"))



if __name__ == '__main__':
    print(multiply(3, 4))
    print(buy("course"))
    print(__name__)
    print("run this")