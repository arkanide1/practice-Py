#iterable
#generator are iterable ,everything that is a generator is iterable 
# but nt everything that is iterable is generator
# for eg : range(100) is a generator so its gonna be iterable
# list is iterable but not generator
# generator is a subset of iterable
def generator_function(n):
    for i in range(n):
        # instead of returning we use yield keyword
        yield i*2


# for item in generator_function(10):
#     print(item)

g= generator_function(10)
next(g)
next(g)
print(next(g))