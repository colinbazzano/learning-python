# list, set, dictionary
# here's one way of doing it
my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)

# var = [param for param in iterable]
my_new_list = [char for char in "hello"]

print(my_new_list)

another_list = [num*2 for num in range(0, 100)]

print(another_list)
# we want a list, where we loop through 0-100, to the power of 2, if it is even
one_last_list = [[num**2 for num in range(0, 100) if num % 2 == 0]]

print(one_last_list)

simple_dict = {
    "a": 1,
    "b": 2
}
# my_dict = {key:value}
my_dict = {key: value**2 for key, value in simple_dict.items()}

print(my_dict)
# key:value*2
another_dict = {num: num*2 for num in [1, 2, 3]}

print(another_dict)

some_list = ["a", 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# we wrap it in a set to avoid duplicates, and wrap it in a list so it's a list not a set, lol
duplicates = list(set([let for let in some_list if some_list.count(let) > 1]))

print(duplicates)
