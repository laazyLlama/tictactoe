#------------------------------------------------------------------------------
#Project Name:     tictactoe
#Description:      TacTacToe made in the languae that is named after a snake
#------------------------------------------------------------------------------
#Author:           laazyLlama
#Date Created:     28/04/2021
#Last Changes:     28/04/2021
#------------------------------------------------------------------------------

#     A   B   C
#   +---+---+---+
# 1 |   |   |   |
#   +---+---+---+
# 2 |   |   |   |
#   +---+---+---+
# 3 |   |   |   |
#   +---+---+---+

def print_horizontal_line():
    print("   +---+---+---+")

def print_board():
    print("     A   B   C  ")
    print_horizontal_line()
    for i in range(3):
        print(" " + str(i + 1) +" |   |   |   |")
        print_horizontal_line()

print_board()
