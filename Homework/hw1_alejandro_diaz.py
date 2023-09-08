"""
Homework 1
Name: Alejandro Diaz
Due Date: 08/24/23

This homework assignment serves as practice using loops and variables.
The idea is to implement a security program that asks various questions.
Each question is unique in that each one requires a specific task from the user.
"""

from random import randint, random

# Variables needed for the while loop to function:
test_complete = 0
minimum_required_correct = 3
name = ""

# While loop that continuously runs until all questions are answered correctly:
while test_complete == 0:
    print("Welcome! You will be asked several questions to verify that you are human... \n"
          + "You may not leave until you do so.\n")

    print("To begin, please enter your name: ")
    name = input().upper()

    # First Test: -------------------------------------------------------------------------
    a = randint(1, 11)
    b = randint(1, 11)
    random_operator = randint(1, 4)
    correct_answer = 0

    print("\n1. The first question is designed to test your ability to understand basic math. \n"
          "Given variables a = " + str(a) + " and b = " + str(b) + ":")

    if random_operator == 1:
        print("What is a + b: ")
        correct_answer = a + b

    elif random_operator == 2:
        print("What is a - b: ")
        correct_answer = a - b

    elif random_operator == 3:
        print("What is a * b: ")
        correct_answer = a * b

    else:
        print("What is a / b to the nearest int: ")
        correct_answer = a // b

    # Award a token if correct answer was given. If not, print disappointment and end program:
    q1_response = input()

    if (q1_response.lstrip('-').isdigit()) and (int(q1_response) == correct_answer):
        print("That is correct. Moving on to the next question...")
    else:
        break

    # Second Test: ------------------------------------------------------------------------
    randomizer = randint(1, 11)
    if randomizer > 4:
        monkey1 = "CESAR"
    else:
        monkey1 = "MAURICE"
    monkey1_time = round((random() * 10.0), 2)  # This will concat the float to 2 decimal places

    randomizer = randint(1, 11)
    if randomizer > 4:
        monkey2 = "KOBA"
    else:
        monkey2 = "ROCKET"
    monkey2_time = round((random() * 10.0), 2)

    monkey_winner = ""
    monkey_winner_time = 0.0
    if monkey1_time > monkey2_time:
        monkey_winner = monkey2
        monkey_winner_time = monkey2_time
    elif monkey2_time > monkey1_time:
        monkey_winner = monkey1
        monkey_winner_time = monkey1_time
    else:
        monkey_winner = "NOBODY"

    print("\n2. The second question is designed to test your reasoning & deductive skills. \n"
          "Suppose there are two monkeys in a race for world domination. The first monkey, "
          + monkey1 + ", can dominate the world in approximately " + str(monkey1_time) + " seconds. \n"
          + "The second monkey, " + monkey2 + " can do it in " + str(monkey2_time) + " seconds. \n\n"
          + "Which monkey will conquer the world first (Enter 'NOBODY' if equal): ")

    # Award a token if correct answer was given. If not, print disappointment and move on:
    if input().upper() == monkey_winner:
        print("That is correct. Moving on to the next question...")
    else:
        break

    # Third Test: -------------------------------------------------------------------------
    robot_flag = 0

    print("\n3. The third question is designed to test your memorization & cognitive functionality.")

    for i in range(3):
        if robot_flag == 0:     # If anything fishy happens within the for loop, robot_flag will be triggered

            # FOR LOOP Question 1:
            if i == 0:
                print("Please enter your name: ")
                given_name = input().upper()

                # I chose to structure question 3 this way to make use of 'continue':
                if given_name == name:
                    continue
                else:
                    print("Are you sure that's your name?")
                    given_name = input().upper()

                    if given_name != name:
                        robot_flag = robot_flag + 1

            # FOR LOOP Question 2:
            if i == 1:
                print("Is the number of letters of both monkey's names from Question 2 greater than yours? (YES/NO)")
                correct_response = ""

                if len(monkey1) + len(monkey2) > len(name):
                    correct_response = "YES"
                else:
                    correct_response = "NO"

                if input().upper() != correct_response:
                    robot_flag = robot_flag + 1

            # FOR LOOP Question 3:
            if i == 2:
                print("How long did it take for " + monkey_winner + " to conquer the world? ")

                if float(input()) != monkey_winner_time:
                    robot_flag = robot_flag + 1

        else:
            break

    # End of for loop

    if robot_flag:
        break
    else:
        test_complete = 1

# End of while loop

# I chose 'test_complete' as an integer to fulfil the requirement of using at least one "Truthy" value:
if test_complete:
    print("\nThis program has confirmed that you are a human. Listen closely...\n"
          + "There will be a green 'Dwayne The Rock Johnson' boat underneath Dr. Yanyan's lecture podium in UHAL 132.\n"
          + "This information is TOP SECRET. Do not reveal this to anyone else!")
else:
    print("Your response was incorrect. Goodbye.")
