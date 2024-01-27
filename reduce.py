# reduce doesn't come as part of python buit functions
# in order to use it we have to import this
# from functools import reduce

from functools import reduce

my_li = [1, 2,3]


def accumulator(acc, item):
    print(acc, item )
    return acc 

# reduce(function , data, initial value )
# function -> takes to parameteres
# accumulator(acc , item )


print(reduce(accumulator, my_li, 0))
print(my_li)

