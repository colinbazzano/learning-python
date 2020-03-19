"""lambda expressions

lambda expressions are functions that are anonymous and meant to only be used once, then "thrown away"

"""

# lambda param: action(param)
my_list = [1, 2, 3]


# def multiply_by2(item):
#     return item * 2

# instead of creating a function, and passing it to the print below, we specify
# lambda, with the param of item, and multiply by 2 for the my_list content
print(list(map(lambda item: item*2, my_list)))

new_list = [5, 4, 3]

print(list(map(lambda item: item**2, new_list)))


# list sorting

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# print(list(lambda tup: tup.sort(key=lambda x: x[1])))

a.sort(key=lambda x: x[1])
print(a)
