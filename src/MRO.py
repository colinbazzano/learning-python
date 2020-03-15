# MRO - Method Resolution Order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # what will this print out?
print(D.mro())  # check the order flow!


# Another neat example

class X:
    pass


class Y:
    pass


class Z:
    pass


class A2(X, Y):
    pass


class B2(Y, Z):
    pass


class M(B2, A2, Z):
    pass


# predicted order: M -> B -> Y -> Z -> A -> -> X -> Z -> object
# answer: M -> B -> A -> X -> Y -> Z -> object
print(M.mro())
# Algorithm used - Depth First Search
