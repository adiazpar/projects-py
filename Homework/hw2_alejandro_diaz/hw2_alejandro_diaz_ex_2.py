"""
Homework 2 Exercise 2
Name: Alejandro Diaz
Due Date: 09/22/23

Exercise 2:
Add try and except statements to the previous exercise (the collatz sequence) to detect whether
the user enters a non-integer value. Normally, the int() function will raise a ValueError error if it
is passed a non-integer string, as in int('puppy'). In the except clause, print a message to the user
saying they must enter an integer.
"""


def collatz(number):
    value = 0

    # Checks to see if the given number is even:
    if number % 2 == 0:
        value = number//2

    # Checks to see if the given number is odd:
    elif number % 2 != 0:
        value = 3 * number + 1

    print(value)
    return value
# end of collatz


valid = False

while not valid:
    # Prompting user input for positive integer:
    print("Please enter a positive integer: ")
    response = input()

    # Error checking non-integer responses:
    try:
        # Trying to cast to int to check for value error:
        response = int(response)

        # Error checking non-positive integers:
        if response > 0:
            valid = True
            while response != 1:
                response = collatz(response)
        else:
            print("Not a positive integer...")

    except ValueError:
        print("Must enter an integer...")
# end of while loop
