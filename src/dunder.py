
"""dunder methods

special methods __likethis__ are dunder methods that we use

some cases, you do in fact replace dunder methods, something like __str__ or __repr__

"""

# in this case, the __str__ method is only replaced for the Toy class


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': "Yoyo",
            'has_pets': False
        }

    def __str__(self):
        return f"{self.color}"

    # you could do this but also maybe dont
    def __len__(self):
        return 5

    def __call__(self):
        return("I've been called!")

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)

print(action_figure.__str__())
print(action_figure())  # normally do NOT do this, but for reference
print(action_figure['name'])
