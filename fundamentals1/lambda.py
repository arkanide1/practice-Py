#lambda expressions

#  how to use it lambda param: action(param)
# we use lambda for functions that we wanna use just one time 

from functools import reduce

li=[1,2,3]

def multiply_by2(item):
    return item*2
# instead of using multiply_by2 fct we use lambda map(lambda ... , data) 
print(list(filter(lambda item : item%2 , li )))
print(list(map( lambda item: item*2 , li )))
print(li)
print(reduce( lambda acc, item :acc+item  , li))

# lambda exercice 

li2= [5,4,3]
print(list (map( lambda item : item*item , li2)))

li3 = [(0,2) , (4,3), (10 , -1) , (9,9),]

li3.sort(key= lambda item : item[1])
print(li3)