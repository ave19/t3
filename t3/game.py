#
# Tic Tac Toe Game Manager
#

import t3.board

class Game(object):

        def __init__(self):
            self.board = t3.board.Board()
            self.player_one = t3.player.Player()
            self.player_two = t3.player.Player()
