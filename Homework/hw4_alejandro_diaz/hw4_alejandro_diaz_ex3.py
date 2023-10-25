"""
Homework 4 Exercise 3
Name: Alejandro Diaz
Due Date: 10/24/23

Exercise 3:
Write a program that uses regular expressions to make sure the password string it receives
through input (either through the input() function or command line arguments) is strong.

A strong password in this exercise is defined as one that:

    (1) is at least eight characters long,
    (2) contains both uppercase and lowercase characters, and
    (3) has at least one digit

You may assume there is no other special characters such as punctuations.
You may need to test the password string against multiple regex patterns to validate its strength
as described above (Note: Please only use regexes).
"""
import re

if __name__ == "__main__":
    password_pattern = ("^(?=.*?[A-Z])"         # Checks for at least one uppercase letter
                        "(?=.*?[a-z])"          # Checks for at least one lowercase letter
                        "(?=.*?[0-9])"          # Checks for at least one digit
                        #"(?=.*?[#?!@$%^&*-])"   # Checks for at least one special character
                        ".{8,}$")               # Checks for at least 8 characters in the string

    print("Please enter a password: ")
    password = input()

    if( re.match(password_pattern, password) ):
        print("Good job, you have entered a valid password...")
    else:
        print("This is an invalid password!")
