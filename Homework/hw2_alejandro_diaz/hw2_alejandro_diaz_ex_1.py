"""
Homework 2 Exercise 1
Name: Alejandro Diaz
Due Date: 09/22/23

Exercise 1:
Write a function named collatz() that has one argument called number. If number is even, then
collatz() should print number // 2 and return this value. If number is odd, then collatz() should
print and return 3 * number + 1

This program lets the user enter an integer and keeps calling collatz() on that number
until the function returns value 1. (Amazingly enough, this sequence actually works for any
integer—sooner or later, using this sequence, you’ll arrive at 1. Even mathematicians aren’t sure
why. Your program is exploring what’s called the Collatz sequence, sometimes called “the
simplest impossible math problem.”)
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


# Prompting user input for positive integer:
print("Please enter a positive integer: ")
response = int(input())

if response > 0:
    while response != 1:
        response = collatz(response)
else:
    print("Not a positive integer...")
