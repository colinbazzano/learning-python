# """guessing game

# doesn't entirely work but shows the powers are ARGV and getting user input in the terminal

# """

from random import randint
import sys
# generate a number 1 through 10

# get an input from user

# check that input is a number 1 through 10

# check if number is the right guess
# otherwise ask again


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("You are a god!!!!!!!")
            return True
        else:
            print("guess again!")
    else:
        print("...a number between 1-10...    ")


if __name__ == "__main__":
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input("Guess a number, one through ten ->   "))
            if(run_guess(guess, answer)):
                break

        except ValueError:
            print("Please enter a number")
