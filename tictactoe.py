#------------------------------------------------------------------------------
#Project Name:     tictactoe
#Description:      TacTacToe made in the languae that is named after a snake
#------------------------------------------------------------------------------
#Author:           laazyLlama
#Date Created:     28/04/2021
#Last Changes:     01/05/2021
#------------------------------------------------------------------------------

import random

# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+

"""
def print_start():
    print("****************************************") #40 spaces
    print("*                                      *")
    print("*               Welcome:               *")
    print("*                  to                  *")
    print("*             Tic-Tac-Toe              *")
    print("*                                      *")
    print("*          PV<P>        PV<E>          *")
    print("*                                      *")
    print("*                                      *")
    print("****************************************")

def get_cell(coordinate):
    if int(coordinate[0]) <= 3:
        print("true")


print_start()
print_board()
for i in range(9):
    if (i % 2) == 0:
        choise = input("  Player_1 > ")
    else:
        choise = input("  Player_2 > ")
    print(choise)
    get_cell(choise)
    print_board()
"""

class Game:
    def __init__(self):
        self.board = [str(i + 1) for i in range(9)]
        self.winner = None

    def print_board(self):
        print("+---+---+---+")
        for line in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(line) + " |")
            print("+---+---+---+")

    def get_avilable_moves(self):
        valid_moves = []
        for cell in self.board:
            if (cell != 'X') and (cell != 'O'):
                valid_moves.append(cell)
        return valid_moves

    def make_move(self, cell_index, symbol):
        self.board[cell_index] = symbol


class Player:
    def __init__(self, symbol):
        self.symbol = symbol


game = Game()
game.make_move(1, 'X')
game.print_board()
print(game.get_avilable_moves())
