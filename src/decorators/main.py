"""decorators

@staticmethods
@classmethods

"""


def hello():
    print("helllllloooo")


greet = hello
del hello
print(greet())

# because functions are first class citizens, greet still works even though we have deleted
# the hello function.

# Higher order functions


def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func
