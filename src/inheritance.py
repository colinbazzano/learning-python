# Inheritance

""" users

there are wizards, archers, etc.

"""


class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows}")


wizard1 = Wizard("Merlin", 5000)
archer1 = Archer("Robin", 100)
# wizard1.attack()
# archer1.attack()
# archer1.sign_in()  # from the base class
# will return True, because wizard1 is an instance of Wizard
print(isinstance(wizard1, Wizard))
# this will also return True because it is an instance of User as the base class
print(isinstance(wizard1, User))
# this finally, will return True because it inherits from object -> User -> Wizard
print(isinstance(wizard1, object))
