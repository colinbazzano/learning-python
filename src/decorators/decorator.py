# Decorator

"""decorator

super boosts our function. In this case we are wrapping the hello/bye function
with our wrap_func in our my_decorator function
"""

# Decorator Patterns


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


@my_decorator
def bye(greeting):
    print(greeting)


hello("yoyo")
bye("yoyoinks")
