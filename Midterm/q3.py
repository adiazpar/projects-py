"""
Midterm Question 3
Name: Alejandro Diaz
Due Date: 10/16/23

"""

import random

if __name__ == "__main__":
    n = random.randint(1, 7)
    print("n is " + str(n))

    # Generate the first n squares that are not divisible by 2:
    out = []
    num, i = 0, 0

    while num != n:
        if pow(i, 2) % 2 != 0:
            num += 1
            out.append(pow(i, 2))
        i += 1

    # I can replace the above with a lambda function:

    # Print the output:
    print("The first " + str(n) + " square(s) that are not divisible by 2 are: " + str(out))
