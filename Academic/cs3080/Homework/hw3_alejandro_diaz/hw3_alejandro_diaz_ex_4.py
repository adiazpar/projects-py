"""
Homework 3 Exercise 4
Name: Alejandro Diaz
Due Date: 10/06/23

Exercise 4:
In this exercise we are going to create a Tic-Tac-Toe game.

    1. Create the data structure
        – Nine slots that can each contain an X, an O, or a blank.
        – To represent the board with a dictionary, you can assign each slot a string-value key.
        – String values in the key-value pair to represent what’s in each slot on the board:
                - "X"
                - "O"
                - " "
    2. Create a function to print the board dictionary on the screen
    3. Add the code that allows the players to enter their moves

This isn’t a complete tic-tac-toe game — for instance, it does not check whether a player has
won — but it’s enough to see how data structures can be used in programs. You can find the
answer in the textbook, but please use it to guide yourself how to implement the code. You are
free to implement a complete game if you like.
"""


def print_board(board):
    num_rows = len(board)           # Calculates the number of items in the board list
    num_cols = len(board[0])        # Calculates the number of items in the dictionary

    print("\t\t  0:  1:  2: ")
    print("\t- - - - - - - - -")

    for i in range(num_rows):
        print("\t" + str(i) + ":\t|", end='')

        for j in range(num_cols):
            print(" " + board[i].get((i, j)), end=' |')
        print(end='\n')

    print("\t- - - - - - - - -")


def run_game(board):
    # Initializing local variables:
    turn = 0
    game_over = False

    # Loop to continue the game while it isn't over:
    while not game_over:
        # Algorithm to switch players at the start of each turn:
        if turn:
            current_player, turn = 'X', 0
        else:
            current_player, turn = 'O', 1

        print_board(board)
        print("\tPlayer " + current_player + ", what is your move?\n"
              + "\t(x y): ", end="")

        # Prompting user to enter a coordinate:
        res_x, res_y = validate_coord(board)

        # Assigning a board space to the current player's shape:
        board[res_x][(res_x, res_y)] = current_player
        print("")

        if check_winner(board, current_player):
            game_over = True

            print_board(board)
            print("\tGame Over! The results are in... \n\tPlayer " + current_player + " won!")


def check_winner(board, player):
    # Raise this flag when a winner is found:
    flag = False

    # Check for a diagonal win:
    if (board[0][(0, 0)] == board[1][(1, 1)] == board[2][(2, 2)] == player or
            board[0][(0, 2)] == board[1][(1, 1)] == board[2][(2, 0)] == player):
        flag = True

    # Checking the coordinates:
    f_row_coord = list(board[0].keys())
    s_row_coord = list(board[1].keys())
    t_row_coord = list(board[2].keys())

    for x in range(len(board)):
        for y in range(len(board[0])):
            curr = (x, y)       # Get the current coordinates

            # Only check the middle square and its consecutive spaces:
            if (curr == s_row_coord[0] or curr == s_row_coord[1] or curr == s_row_coord[2]
                    or curr == f_row_coord[1] or curr == t_row_coord[1]):

                l_of_curr = (x, y-1) if y == 1 else (x, 0)
                r_of_curr = (x, y+1) if y == 1 else (x, 2)
                u_of_curr = (x-1, y) if x == 1 else (0, y)
                d_of_curr = (x+1, y) if x == 1 else (2, y)

                # Check for horizontal win:
                if y == 1 and player == board[x][curr] == board[x][l_of_curr] == board[x][r_of_curr]:
                    flag = True

                # Check for Vertical win:
                elif x == 1 and player == board[x][curr] == board[x-1][u_of_curr] == board[x+1][d_of_curr]:
                    flag = True


    return flag


def validate_coord(board):
    # Initializing local variables:
    valid_res = False
    x, y = 0, 0

    # Loop that gets user input until a valid response is entered:
    while not valid_res:
        response = input().strip(" ")       # strip method to delete trailing and leading whitespace

        # This section checks to see if there are digits in the response:
        num_digits = 0
        for char in response:
            if char.isdigit():
                num_digits += 1

        # This checks to see if there are specifically 2 digits, and at least 1 space between them:
        if response.count(" ") == 1 and num_digits == 2:
            x, y = response.split()         # split method to split both digits into a list
            x, y = int(x), int(y)           # casting both digits into integers

            # Finally, check to see if the coordinate is open:
            if board[x][(x, y)] == ' ':
                valid_res = True                # valid response flag set to true, exits the loop
            else:
                print("\tThat space has already been taken! \n\t(x y): ", end="")
        else:
            print("\tERROR: Please enter a valid coordinate\n\t(x y): ", end="")

    return x, y


if __name__ == "__main__":
    ttt_board = [
        {(0, 0): ' ', (0, 1): ' ', (0, 2): ' '},
        {(1, 0): ' ', (1, 1): ' ', (1, 2): ' '},
        {(2, 0): ' ', (2, 1): ' ', (2, 2): ' '},
    ]

    # Print the rules (yes, need to work on not hard coding this):
    print("+-----------------------------------------------------------------------------------------------+\n"
          + "| Welcome to Tic-Tac-Toe!\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|\n"
          + "| RULES: When it's your turn, enter a coordinate (x y) to fill the space with your shape.\t\t|\n"
          + "| For example, you would enter 0 0 to fill the top left space, or 2 2 to fill the bottom right.\t|\n"
          + "+-----------------------------------------------------------------------------------------------+\n")

    run_game(ttt_board)
