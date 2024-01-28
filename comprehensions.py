# we use them with 3 data types :
# list , set , dictionary

# list comprehension is used to create lists in python in a faster way

mylist=[]

for char in "hello":
    mylist.append(char)


# instead of doing this 🔼
# we can do this 
# syntaxe [param for param in iterable ]
my_li= [ char for char in "hello" ]

print(mylist)
print(my_li)

numlist = [num*2 for num in range(100)]
numlist2= [(num**2) for num in range(100)  if not num%2       ]

print(numlist2)

