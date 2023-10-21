"""
Midterm Question 4
Name: Alejandro Diaz
Due Date: 10/16/23

"""

if __name__ == "__main__":

    # Declaring string variable to be operated on:
    string = "It was a bright cold day in April, and the clocks were striking thirteen."
    print(string)

    # Creating dictionary to store unique characters
    unique = {}
    for char in string:
        # Increment unique count for the char in the dictionary:
        if char.isalpha():  # old if statement: if char != ' ' and char != '.' and char != ','
            unique[char] = unique.get(char, 0) + 1

            # Another method:
            #unique.setdefault(char, 0)
            #unique[char] += 1

    # Finding the most used character and its occurrences:
    i = 0
    most_occurred = ' '
    for char in unique:
        if unique.get(char) > i:
            i = unique.get(char)
            most_occurred = char

    print("The most common character: " + most_occurred)
    print("Number of occurrences: " + str(i))

    # Counting the number of words:
    word_list = string.split()

    """
    THIS IS YOUR OLD CAVEMAN CODE, THE ABOVE CAN REPLACE IT!!!!!!!!
    num_words = 0
    for char in string:
        if char == ' ':
            num_words += 1

    if num_words > 1:
        num_words += 1
    else:
        num_words = 0
    """

    print("\nThe number of total words in the string: " + str(len(word_list)))



