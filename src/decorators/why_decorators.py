# Why use decorators

"""we want to make a performance decorator

for making the decorator:
    1. create the function, which takes in a function as a param
    2. create a wrapper function that will take *args and **kwargs (which are passed to the function from first param)
    3. return the inner param function, and then the wrapper function

    in this case, we have made a wrapper function that calculates the time before running the function
    and after running the function, then prints the time it took!

    neat.

"""

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"took {end-start} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(29999399):
        i*5


long_time()
