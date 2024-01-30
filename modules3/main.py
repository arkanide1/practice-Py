# some useful modules

from collections import Counter , defaultdict , OrderedDict

li =[1,2,3,4,5, 5 ,4]

print(Counter(li))
# counter creates a dict that keeps track of hw many times an item occured

dictionary = defaultdict(lambda:"does not exist" , {'a':1,'b':2})
# gives default value to the keys which doesnt exist in the dict
print(dictionary['c'])
print(dictionary['d'])

d1= OrderedDict()
d1['a']=1
d1['b']=2

d2= OrderedDict()
d2['a']=1
d2['b']=2

print(d2 == d1)