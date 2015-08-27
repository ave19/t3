#
#
#

class Board(object):
    
    min_board = 0
    max_board = 3^9
    
    def __init__(self, *args, **kwargs):
        self._data = {}
        
    @property
    def board(self):
        return self._data['board']
    
    @board.setter
    def board(self, new_board):
        if new_board >= self.min_board and new_board <= self.max_board:
            self._data['board'] = new_board
        else:
            raise ValueError("board must be between %s and %s, inclusive." % (self.min_board, self.max_board))