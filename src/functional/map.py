
# def multiply_by_2(lst):
#   new_list = []
#   for item in lst:
#     new_list.append(item*2)
#   return new_list

# print(multiply_by_2([2, 5, 4]))

# note how the function is pure and even passing it a list does not change that list
my_list = [1, 2, 3]


def multiply_by_2(item):
    return item*2


print("NEW LIST:", list(map(multiply_by_2, my_list)))
print("MY LIST:", my_list)
