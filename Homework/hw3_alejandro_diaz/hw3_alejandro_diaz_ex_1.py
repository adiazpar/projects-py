"""
Homework 3 Exercise 1
Name: Alejandro Diaz
Due Date: 10/06/23

Exercise 1:
You have a list of lists where each value in the inner lists is a one-character string, like this:

    grid = [    ['.', '.', '.', '.', '.', '.'],
                ['.', 'O', 'O', '.', '.', '.'],
                ['O', 'O', 'O', 'O', '.', '.'],
                ['O', 'O', 'O', 'O', 'O', '.'],
                ['.', 'O', 'O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O', 'O', '.'],
                ['O', 'O', 'O', 'O', '.', '.'],
                ['.', 'O', 'O', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.']]

You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn
with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase
going right, and the y-coordinates increase going down. Copy the previous grid value, and write
code that uses it to print the image.

                ..OO.OO..
                .OOOOOOO.
                .OOOOOOO.
                ..OOOOO..
                ...OOO...
                ....O....

Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then
grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print a newline. Then
your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing
your program will print is grid[8][5]. Also, remember to pass the end keyword argument to print()
if you don’t want a newline printed automatically after each print() call. Save your code as
hw3_firstname_lastname_ex_1.py
"""

# Creating the character grid:
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

# Assigning values to respective grid sizes:
x_value = len(grid[0])
y_value = len(grid)

# Printing the character grid with 2 for loops:
for i in range(x_value):
    for j in range(y_value):
        print(grid[j][i], end='')

    print(end='\n')
