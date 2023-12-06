"""
Homework 3 Exercise 2
Name: Alejandro Diaz
Due Date: 10/06/23

Exercise 2:
Develop a program that counts the number of occurrences of each character in a string, including
letters, punctuations, and white spaces. Letters are case sensitive (‘T’ and ‘t’ are different).
Store the result in a dictionary, with the characters as the keys, and number of occurrences as their
values. You can use the following string to test (but your code should work with any string input):

    The quick brown fox jumps over the lazy dog.

Note that this string contains all the letters of the English alphabet.
Finally, use the module pprint for pretty printing of dictionaries.

    import pprint
    pprint.pprint(dictionary)
    or
    spam = pprint.pformat(dictionary) # Pretty text as a string value
    print(spam)
"""

# Importing pprint module:
import pprint

# Input string to be used for the program:
response = "\0"

# Prompting user to input a value:
print("Please enter a string: ")
response = input()

# Creating dictionary to store unique characters
unique = {}

# Iterating over every char in the given string:
for char in response:
    # Incriment unique count for the char in the dictionary:
    unique[char] = unique.get(char, 0) + 1

# Printing the dictionary:
pprint.pprint(unique)