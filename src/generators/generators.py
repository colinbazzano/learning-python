"""generators

range(100)
list(range(100))
below, the function creates an item in the list, adds it, then repeats, it does not make a big list then fill it.
the list exists in memory

"""


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


my_list = make_list(100)
print(my_list)


def generator_function(num):
    for i in range(num):
        yield i


# for item in generator_function():
#     print(item)

g = generator_function(10)

print(g)
print(next(g))
print(next(g))
