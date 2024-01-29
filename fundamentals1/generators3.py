def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
special_for([1,2,3])


class MyGen():
    def __init__(self , first , last ):
        self.first = first 
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if (self.first < self.last):
            num = self.first
            self.first+=1
            return num
        raise StopIteration






gen = MyGen(3, 10)
for i in gen:
    print(i)