# higher order functions !
# map , filter , zip and reduce
"""
def multiply_by2(li):
    newlist=[]
    for item in li:
        newlist.append(item*2)
    return newlist
"""
def multiply_by2(item):
    return str(item)+"!"

# map(action ,[data that we wanna that action upon])

li=[1,2,3]
print(list(map(multiply_by2, li)))
print(li)