def isdividedby2(item):
    if (item % 2 == 0):
        return item
    
def addstr(item):
    return str(item)+ " is divided by 2"

li = [1, 2, 3, 4, 5, 6, 7, 8]
dividedlist= list(map( addstr , list(filter(isdividedby2, li))))


for item in dividedlist:
    print(item)
