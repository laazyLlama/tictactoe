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

def print_start():
    print("****************************************") #40 spaces
    print("*                                      *")
    print("*               Welcome:               *")
    print("*                  to                  *")
    print("*             Tic-Tac-Toe              *")
    print("*                                      *")
    print("*          PV<P>        PV<E>          *")
    print("*                                      *")
    print("****************************************")

def print_horizontal_line():
    print("   +---+---+---+")

def print_board():
    print("\n\n     A   B   C  ")
    print_horizontal_line()
    for i in range(3):
        print(" " + str(i + 1) +" |   |   |   |")
        print_horizontal_line()
    print(" ")

print_start()
print_board()
for i in range(9):
    if (i % 2) == 0:
        input("  Player_1 > ")
    else:
        input("  Player_2 > ")
    print_board()
