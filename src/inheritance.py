# Inheritance

""" users

there are wizards, archers, etc.

"""


class User:
    # def __init__(self, email):
    #     self.email = email

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

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


hb1 = HybridBorg("Jeff", 50, 100)
print(hb1.run())

# wizard1 = Wizard("Merlin", 5000, "merlin@wizards.com")
# archer1 = Archer("Robin", 100)
# # wizard1.attack()
# # archer1.attack()
# # archer1.sign_in()  # from the base class
# # will return True, because wizard1 is an instance of Wizard
# # print(isinstance(wizard1, Wizard))
# # # this will also return True because it is an instance of User as the base class
# # print(isinstance(wizard1, User))
# # # this finally, will return True because it inherits from object -> User -> Wizard
# # print(isinstance(wizard1, object))
# print(wizard1.email)

# # introspection - the ability to determine the type of an object at runtime
# print(dir(wizard1))  # give an instance and it returns what it has access to
