# A Hub for things related to Python

## Four Pillars of OOP:

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

## Folders found in /src:

### classes

    all things basic Python classes, such as the four pillars of OOP, inheritance, __init__, etc.

### decorators

    creating and using Python decorators to provide super boosted functionality to your functions

### errors

    part of programming is handling errors, this folder covers that

### functional

    Python is a powerful OOP language, though it can also be used in a more functional manner of programming.

### generators

    a great way to solve some problems using generators that are a different approach to what you'd normally see

### testing

    testing your code is essential, and this covers some ways you can test your code and improve your code to cover
    edge cases.
    * helpful: python3 -m unittest - allows you to run all tests in the files
    * adding -v, which stands for verbose, will give more information about each test

    in the sys folder, you will find more testing for a random integer guessing game

# Other useful things:

    iterable: under the hood, it has the __iter__ function, and can be looped through
    generators: they are all iterable

    if __name__ == "__main__":
    this is given to a file as the current file. as you run it it gets the default __main__ if that's the file you are running. If you are confused, go into a file and print(__name__) when you are inside of the file.

    when you see a Class that has __main__.ClassName that means that it was created inside that file.

    pipenv for creating virtual environments. This will allow you to use multiple versions of something without it causing large errors

### Python Built-In Modules

    You need to import some things from Python that have already been installed, and we call those built-in modules. Things like time/datetime, random, etc.
