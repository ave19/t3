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


        def round(self, player):
            if not type(player) is t3.player.Player:
                raise ValueError("player must be Player, not %s" % (type(player)))

            try:
                move = player.move(self.board)
                self.board.move(move, player.symbol)
                self.turn += 1
            except ValueError as v:
                print "\nSorry, %s" % v


        def play(self):
            self.two_player()

        def two_player(self):
            self.players.append(t3.player.Player("Player One", "X"))
            self.players.append(t3.player.Player("Player Two", "O"))
            while not self.board.is_full():
                player = self.next_player()
                self.round(player)
                if self.board.has_winner():
                    player.win(self.board)
                    player = self.next_player()
                    player.lose(self.board)
                    break
                if self.board.is_full():
                    player.draw(self.board)
                    player = self.next_player()
                    player.draw(self.board)
                    break
