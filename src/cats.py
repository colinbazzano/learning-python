class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Cat object with 3 cats


cat1 = Cat("Tiff", 1)
cat2 = Cat("Gregory", 3)
cat3 = Cat("Harold", 12)

# Create a function that finds the oldest cat


def oldest_cat(*args):
    return max(args)


# Print out: "The oldest cat is x years old" x will be the oldest cat age
print(
    f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old")
