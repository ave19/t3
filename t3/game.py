#
# Tic Tac Toe Game Manager
#

import t3.board
import t3.player

class Game(object):

        def __init__(self):
            self.board = t3.board.Board()
            self.players = []
            self.turn = 0

        def next_player(self):
            number_of_players = len(self.players)
            if self.turn >= number_of_players:
                self.turn = 0
            return self.players[self.turn]

        def show_board(self):
            print "\nThe Board:\n%s" % self.board

        def show_moves_left(self):
            print "\nAvailable Moves:\n%s" % self.board.show_empty_spots()

        def round(self, player):
            if not type(player) is t3.player.Player:
                raise ValueError("player must be Player, not %s" % (type(player)))

            self.show_board()
            self.show_moves_left()

            try:
                move = player.collect_move()
                self.board.move(move, player.symbol)
                self.turn += 1
            except ValueError as v:
                print "\nSorry, %s" % v


        def play(self):
            self.players.append(t3.player.Player("Player One", "X"))
            self.players.append(t3.player.Player("Player Two", "O"))
            while not self.board.is_full():
                player = self.next_player()
                self.round(player)
                if self.board.has_winner():
                    print "\nCongratulations %s, you win!" % player.name
                    break
                if self.board.is_full():
                    print "\nIt's a tie!\n"
