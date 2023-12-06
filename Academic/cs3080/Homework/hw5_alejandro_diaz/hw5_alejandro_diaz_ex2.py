"""
Homework 5 Exercise 2
Name: Alejandro Diaz
Due Date: 11/09/23

Exercise 2:
Use a generator function or generator expression (you don’t need to implement both) to find the
first n Pythagorean triplets, where n is an integer like 1, 2, 3, and so on.

A triplet (x, y, z) is called a Pythagorean triplet if x*x + y*y == z*z,
where x/y/z are all integers (0 not included).

You may want to use the integers() and take(n, seq) functions explained in class. Implement the
generator with name pyt, and then you could do something like this to get the first n triplets if n=10:

    print(take(10, pyt))

    And the output would be (notice all x/y/z are in a tuple):
    [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17),
    (12, 16, 20), (15, 20, 25), (7, 24, 25), (10, 24, 26), (20, 21, 29)]
"""


def integers():
    # Infinite sequence of integers
    i = 1
    while True:
        yield i
        i = i + 1
# End integers


# This function took me about 5 hours to figure out:
def pyt():
    # Inspired from an example problem in generatorExp1.py
    # The idea is that for the tuple (x, y, z), appropriate values will be found.
    # Since x**2 + y**2 = z**2, z will always be the largest number in the equation.
    # This means that z will be defined in the range of infinite integers().
    # The variable y should always be bigger than x, so y is iterable in the range of z,
    # and x is iterable in the range of y...
    # The iterators will only generate outputs for x, y, and z so that the pythagorean equation
    # is satisfied.
    gen_exp = ((x, y, z) for z in integers() for y in range(z) for x in range(y) if x*x + y*y == z*z)

    # Then, for every tuple 'a' in the generated expression 'gen_exp', this
    # function will yield it.
    for a in gen_exp:
        yield a
# End pyt


# take function that was explained in class
def take(n, seq):
    # Returns first n values from the given sequence.
    seq = iter(seq)     # Just in case it is an iterable object, not a generator or iterator
    result = []         # result is a list to store the tuples
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result
# End take


# Main program:
if __name__ == "__main__":
    print(take(10, pyt()))
# End main