class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
# returns True, bc SuperList is a subclass of list
print(issubclass(SuperList, list))
print(issubclass(list, object))
