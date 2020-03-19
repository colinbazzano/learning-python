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


wizard = Wizard("Merlin", 5000)
archer = Archer("Robin", 30)


def player_attack(char):
    char.attack()


# note how they attack
player_attack(wizard)
player_attack(archer)

for char in [wizard, archer]:
    char.attack()

"""polymorphism

we are able to change the attack for wizard and for archer. BUT, we created an attack function for both and we could even make one
on the User class that does a different attack, and still have what we want on our specific class

"""
