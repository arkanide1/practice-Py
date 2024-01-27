def compareTriplets(a, b):
    result=[0,0]
    for i in range(len(a)):
        if (a[i]>b[i]):
            result[0]+=1
        elif a[i]<b[i]:
            result[1]+=1
        else:
            continue
    return result
    
a=[3,2,1]
b=[1,2,3]
print(compareTriplets(a,b))