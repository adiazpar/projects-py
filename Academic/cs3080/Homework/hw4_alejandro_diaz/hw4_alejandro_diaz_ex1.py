"""
Homework 4 Exercise 1
Name: Alejandro Diaz
Due Date: 10/24/23

Exercise 1:
Write three Python classes named Rectangle constructed by a length and width, a Circle
constructed by a radius, and a Square constructed by a side length. All classes should have the
methods that compute:

    - The area
    - The diagonal of the Rectangle or Square class, and the diameter of the Circle class
    - The perimeter

Use as much inheritance as you can. Import the math module, so you can call methods like sqrt().
At the end of the code, use these classes and methods to calculate the perimeter of a circle with
a radius that’s half of the diagonal of a rectangle with a length of 20 and width 10.
"""

from math import sqrt, pow, pi


class Rectangle:
    # Constructor for rectangle class:
    def __init__(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    # Method to find the perimeter of a rectangle:
    def find_perimeter(self):
        return (2 * self.length) + (2 * self.width)

    # Method to find the area of a rectangle:
    def find_area(self):
        return self.length * self.width

    # Method to find the diagonal line of a rectangle:
    def find_diagonal(self):
        # Use the pythagorean theorem:
        return sqrt(pow(self.length, 2) + pow(self.width, 2))

    # Overriding the print method to print rectangle stats:
    def __str__(self):
        return ('{0:<10}= Length: {1:<10.2f} Width: {2:<10.2f} Diagonal: {3:<10.2f}'
                .format("RECTANGLE", self.length, self.width, self.find_diagonal()))


class Square(Rectangle):
    # Override the constructor from rectangle class:
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    # Overriding the print method to print square stats:
    def __str__(self):
        return ('{0:<10}= Length: {1:<10.2f} Width: {2:<10.2f} Diagonal: {3:<10.2f}'
                .format("SQUARE", self.length, self.width, self.find_diagonal()))


class Circle:
    # Constructor for circle class:
    def __init__(self, new_radius):
        self.radius = new_radius

    def find_circumference(self):
        return 2 * pi * self.radius

    def find_area(self):
        return pi * pow(self.radius, 2)

    def find_diameter(self):
        return 2 * self.radius

    # Overriding print method to display circle stats:
    def __str__(self):
        return ('{0:<10}= Radius: {1:<10.2f} Circumference: {2:<15.2f}'
                .format("CIRCLE", self.radius, self.find_circumference()))


# Method to do the thing that the question asks me to do:
def do_something_funky():
    print("Doing something funky...")

    # Create a rectangle with length of 20 and width of 10:
    rect = Rectangle(20, 10)
    d = rect.find_diagonal()
    print(rect)

    # Creating a funky circle where radius is half the length of the diagonal of rect:
    circ = Circle(d/2)
    print(circ)


# This is the main class for the main program loop:
if __name__ == "__main__":
    do_something_funky()
