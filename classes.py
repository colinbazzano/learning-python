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
        print("Run")

    def shout(self):
        print(f"My name is {self.name}")
        return


player1 = PlayerCharacter("George", 23)

print(player1.name)  # prints "George"
print(player1.membership)  # prints "True"
print(player1.shout())
