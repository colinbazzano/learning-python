import main
# importing a file to use!
from main import multiply

import shopping.shopping_cart

# here are two ways you can import. The first one import main brings in everything
print(main.divide(33, 5))
print(multiply(3, 5))
print(shopping.shopping_cart.buy("red"))


# print(__name__)
