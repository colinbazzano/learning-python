
"""errors/ error handling

While we are covered by linters/terminal errors, having your own errors with more
specific explanations is very helpful to future devs/clients

some existing errors:
TypeError
AttributeError
NameError
ReferenceError
IndexError
SyntaxError, etc

to learn more about errors:
https://docs.python.org/3/library/exceptions.html

"""
while True:
    try:
        age = int(input("What is your age?  "))
        10/age
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter an age that is greater than 0")
    else:
        print("Thank you!")
        break
    finally:  # runs regardless at the end
        print("okay, I am finally done!")


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter only numbers, {err}")


print(sum(4, 4))

# you may handle multiple errors like so: except(TypeError, ZeroDivisionError)
