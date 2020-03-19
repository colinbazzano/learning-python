# Filter!

my_list = [1, 2, 3, 4, 5, 6, 7]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)

friends_list = ["Doug", "Ben", "Amber", "Duby", "Karina"]


def d_friends(friend):
    return friend[0] == "D"


print(list(filter(d_friends, friends_list)))
