# OOP
# name and age are attributes


class PlayerCharacter:
    # Class Object Attribute - static
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Run")


player1 = PlayerCharacter("George", 23)

print(player1.name)  # prints "George"
print(player1.membership)  # prints "True"
