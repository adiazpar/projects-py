"""
Homework 5 Exercise 3
Name: Alejandro Diaz
Due Date: 11/09/23

Exercise 3:
The range() function creates a sequence. For very large sequences, this consumes a lot of memory.
You can write a version of range() which does not create the entire sequence, but instead yields
the individual values...

Using a generator will have the same effect as iterating through a sequence but won’t consume as much memory.
Define a generator function called genrange(), which generates the same sequence of values as range(),
without creating a list object.

The original range() function is used as follows:
    - range(stop)                   [v]
    - range(start, stop)            [v]
    - range(start, stop, step)      [v]

For simplicity, genrange() can be used as follows:
    - genrange(stop)                [v]
    - genrange(stop, start)         [v]
    - genrange(stop, start, step)   [v]

where start and step are both optional arguments.
"""


# Method to test how range() works in python:
def range_example(stop=0, start=0, step=1):
    # First case: ----------------------------- |
    print("range() TEST [1]:")
    for i in range(stop):
        print(i, end=' ')

    print("\nSUMMARY: from 0 to " + str(stop) + " every 1 number(s)\n")

    # Second case: ---------------------------- |
    if start:
        print("range() TEST [2]:")
        for i in range(start, stop):
            print(i, end=' ')

        print("\nSUMMARY: from " + str(start) + " to " + str(stop) + " every 1 number(s)\n")

    # Third case: ----------------------------- |
    if step > 1:
        print("range() TEST [3]:")
        for i in range(start, stop, step):
            print(i, end=' ')

        print("\nSUMMARY: from " + str(start) + " to " + str(stop) + " every " + str(step) + " number(s)\n")

    print()


# Method to test how generators work in python:
def genrange(stop=0, start=0, step=1):
    while start < stop:
        yield start
        start += step


# Main program loop:
if __name__ == "__main__":
    # Call to range_example method, takes stop, start, and step as arguments:
    # start & step arguments are optional...
    range_example(10)

    # Call to genrange() method, same parameters and rules:
    for num in genrange(10, 0, 1):
        print(num, end=' ')
# End main
