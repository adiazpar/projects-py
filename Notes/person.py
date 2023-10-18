"""
This is an example of overriding the 'print' method from within a class.
Use this if it comes up in the midterm, this is an uber geek moment:
"""


class Person:

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __str__(self):
        return self.first_name + " " + self.last_name


if __name__ == "__main__":
    author = Person("Al", "Sweigart")
    print(author)
