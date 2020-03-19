# OOP
# name and age are attributes


class PlayerCharacter:
    # Class Object Attribute - static
    membership = True

    def __init__(self, name="Anonymous", age=0):
        if (age > 18):
            # this could be PlayerCharacter.membership, too. ONLY because it is a COA
            self.name = name
            self.age = age

    def run(self):
        return self

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

    # cls for the first argument
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def taking_things(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("George", 23)

# print(player1.name)  # prints "George"
# print(player1.membership)  # prints "True"
# vvvv this is encapsulation, we have these ways of accessing the information that doesn't exist yet vvvvv
print(player1.introduce())
# print(player1.adding_things(2, 5))
# # with class methods you do not need to instantiate the class
# print(PlayerCharacter.adding_things(2, 66))
print(player1.run())
"""private variables

It's a convention to label private variables like so: _name
There are no true private variables in Python, but the underscore says "Hey, please do not change this"

"""
