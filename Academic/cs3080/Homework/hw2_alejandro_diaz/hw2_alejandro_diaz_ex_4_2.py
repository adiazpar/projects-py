"""
Homework 2 Exercise 4.2
Name: Alejandro Diaz
Due Date: 09/22/23

Complicate it by having random lower and upper bounds. Display a message “I am
thinking of a number between lower and upper” and replace lower/upper with the actual
random numbers you generated. The player still has to guess it within 10 tries. Make
sure your lower bound is not higher than you upper bound
"""

from random import randint

# Defining variables that will be used for game functionality:
LOWER_BOUND = randint(0, 1000)
UPPER_BOUND = randint(LOWER_BOUND + 1, 1000)
MAX_TRIES = 10

attempted_tries = 0
number_guessed = False

# Generating a random number for the correct guess:
correct_number = randint(LOWER_BOUND, UPPER_BOUND)

# Introduction to the game:
print("I am thinking of a number between " + str(LOWER_BOUND) + " and " + str(UPPER_BOUND)
      + ". You have " + str(MAX_TRIES) + " tries.")

# Loop checks it the number has been guessed and that the number of attempted tries is less than the maximum allowed:
while not number_guessed and attempted_tries <= MAX_TRIES:
    print("Take a guess.")
    guessed_number = int(input())   # No validation implemented for reading user input here

    # Cases to check if the guessed number is lower, higher, or equal to the correct number:
    if guessed_number < correct_number:
        print("Your guess is too low.")
    elif guessed_number > correct_number:
        print("Your guess is too high.")
    else:
        number_guessed = True

    # Iterate the number of attempted guesses by 1:
    attempted_tries += 1

# When breaking out of the loop, will check if the number was ever guessed:
if number_guessed:
    print("Good job! You guessed my number in " + str(attempted_tries) + " guesses!")
else:
    print("Sorry, the number I was thinking of was " + str(correct_number))
