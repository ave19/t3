#
# A representation of a tic tac toe board
#


class Board(object):

    min_board = 0
    max_board = 3 ** 9

    def __init__(self, *args, **kwargs):
        self._data = {}

    def __str__(self):
        return

    @property
    def map(self):
        return {
            "0": " ",
            "1": "X",
            "2": "O"
        }

    @property
    def board(self):
        return self._data['board']

    @board.setter
    def board(self, new_board):
        if new_board >= self.min_board and new_board <= self.max_board:
            self._data['board'] = new_board
        else:
            raise ValueError("board must be between %s and %s, inclusive." %
                             (self.min_board, self.max_board)
                             )

    def convert_to_character(self, char):
        if char in self.map:
            return self.map[char]
        raise ValueError("cannot convert char: %s" % char)

    # Stolen from: interactivepython.org
    # pythondsConvertinganIntegertoaStringinAnyBase.html
    def convert_to_string(self, n, base=3):
        conversion_map = "0123456789ABCDEF"
        if n < base:
            return conversion_map[n]
        else:
            rv = self.convert_to_string(n // base, base)
            rv = rv + conversion_map[n % base]
            return rv
