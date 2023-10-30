"""
Homework 5 Exercise 1
Name: Alejandro Diaz
Due Date: 11/09/23

Exercise 1:
Write an iterator class ReverseIter, that takes a list and iterates it from the reverse direction.
Hint – use a list as the input argument of your constructor!
"""


class ReverseIter:
    # Constructor for ReverseIter Class:
    def __init__(self, some_list):
        some_list.reverse()
        self.reversed_list = some_list
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.reversed_list):
            result = self.reversed_list[self.i]
            self.i += 1
            return result
        else:
            raise StopIteration()
# End Class ReverseIter


if __name__ == "__main__":
    test_list = [3, 20, 100, 5, 12, 67]

    # Creating the iterator and iterating through it:
    it = ReverseIter(test_list)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
# End main