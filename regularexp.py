import re


pattern = re.compile("([a-z]).([r])")
# with compile instead of using re.search we use pattern.search

string = "search inside of this text this this"

# a =re.search("this" , string)

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
# returns the match from 0 to the end of the word/expression
d = pattern.match(string)
print(b)
print(c)  # return none because there is no full match
print(d)

print(a.span())
print(a.start())  # returns the index of when the match begins
print(a.end())  # returns where it ends
print(a.group()) # returns the part of the string where there is the match 
# print(re.search("this" , string))
# regular expressions gives us a match object
