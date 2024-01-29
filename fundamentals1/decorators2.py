def my_decorator(func):
    def wrapfunc(*arg, **kargs):
        print("********")
        func(*arg , **kargs)
        print("********")

    return wrapfunc

@my_decorator
def hello(greet , name=":)"):
    print(greet, name)
    
g = "hello"
hello(g)