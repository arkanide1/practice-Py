# decorators are those on the classes eg : @classmetod @staticmethod

"""
def hello(fct):
    fct()
def greet():
    print( "still here")


a = hello(greet)
print(a)

"""

# Decorators

def my_decorator(func):
    def wrapfunc():
        print("********")
        func()
        print("********")

    return wrapfunc
# now u created ur first decorator


@my_decorator
def hello():
    print("hello")
    
#hello()


"""
def mydeco(fct):
    def addone():
        print(f"1+{fct()} = {1+fct()}")
    return addone
@mydeco
def sumi():
    return 5

sumi()
"""
# so these decorators can add extra functionality to our functions
# underneath the hood  all it does is literally this 
# a = decorator(hello)
# a()
hello2 = my_decorator(hello)

hello2()