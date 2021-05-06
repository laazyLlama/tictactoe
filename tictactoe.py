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
"""

class Game:
    def __init__(self):
        self.board = [str(i + 1) for i in range(9)]
        self.winner = None

    def print_board(self):
        print("   +---+---+---+")
        for line in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("   | " + " | ".join(line) + " |")
            print("   +---+---+---+")

    def get_avilable_moves(self):
        valid_moves = []
        for cell in self.board:
            if (cell != 'X') and (cell != 'O'):
                valid_moves.append(self.board.index(cell))
        return valid_moves

    def make_move(self, cell_index, player):
        self.board[cell_index] = player.symbol
        self.check_for_win(cell_index, player)

    def check_for_win(self, cell_index, player):
        row_index = cell_index // 3
        row = self.board[row_index * 3:row_index * 3 + 3]
        if all(cell == player.symbol for cell in row):
            self.winner = player

        column_index = cell_index % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        if all(cell == player.symbol for cell in column):
            self.winner = player

        if cell_index % 2 == 0:
            diagonal_left_right = [self.board[i] for i in [0, 4, 8]]
            if all(cell == player.symbol for cell in diagonal_left_right):
                self.winner = player
            diagonal_right_left = [self.board[i] for i in [2, 4, 6]]
            if all(cell == player.symbol for cell in diagonal_right_left):
                self.winner = player


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_valid_move(self, game):
        cell = None
        valid_move = False
        while not valid_move:
            move = input(f" Player '{self.symbol}' >  ")
            try:
                cell = int(move) - 1
                if cell not in game.get_avilable_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print(f"'{move}' is not a valid move!")
        return cell


game = Game()
player1 = Player('X')
player2 = Player('O')
current_player = player1

game.print_board()
while game.get_avilable_moves():
    game.make_move(current_player.get_valid_move(game), current_player)
    game.print_board()
    if game.winner:
        print(f" Player '{current_player.symbol}' has won!")
        break
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
if game.winner == None:
    print(" It's a tie, nobody won!")
