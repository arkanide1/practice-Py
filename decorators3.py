# build a @performance decorator to see how fast my code runs 

from time import time 


def performance(fn):
    def wrapper(*arg , **args):
        t1= time()
        result = fn(*arg , **args)
        t2=time()
        print(f"took : {t2-t1}s")
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000):
        print(i*5)

long_time()

