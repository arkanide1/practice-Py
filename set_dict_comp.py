
myset = {char for char in "hello"}
print(myset)


# dictonaries

simple_dict={
    "a":1,
    "b":2,
    "c":3,
}
import random
randchar=[char for char in "abcdefghijklmnopqrstuvwxyz"]


my_dict ={ key + random.choice(randchar):value**2 for key,value in simple_dict.items()}

print(my_dict)

mydict2= {num:num*2 for num in [1,2,3]}
print(mydict2)