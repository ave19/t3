#
# A representation of a tic tac toe board
#


class Board(object):

    min_board = 0
    max_board = 3 ** 9
    string_map = { '0': ' ', '1': 'X', '2': 'O' }

    def __init__(self, *args, **kwargs):
        self._data = {}
        self.reset_board()


    def __str__(self):
        rv = "%s|%s|%s\n-|-|-\n%s|%s|%s\n-|-|-\n%s|%s|%s" % (
            tuple([ self.string_map[x] for x in list(self.board) ])
            )
        return rv


    @property
    def board(self):
        # we want the base 3
        return self._data['board']


    @property
    def b10(self):
        return self.convert_to_base10(self.board)


    @board.setter
    def board(self, new_board):
        # A board must be a nine character base 3 string.
        if type(new_board) is not str:
            raise ValueError("Board must be a 'str, not '%s'" % type(new_board))

        if len(new_board) is not 9:
            raise ValueError("Board must be 9 characters long")

        if self.convert_to_base10(new_board) < self.min_board:
            raise ValueError("Value %s is below %s." %
                (new_board, self.min_board))

        if self.convert_to_base10(new_board) > self.max_board:
            raise ValueError("Value %s is above %s." %
                (new_board, self.max_board))

        self._data['board'] = new_board


    def reset_board(self):
        self.board = '000000000'


    def convert_to_base3(self, n, base=3):
        from_map = "0123456789"
        to_map = "012"
        rv = self.rebase(str(n), from_map, to_map)
        return rv.zfill(9)


    def convert_to_base10(self, n, base=10):
        from_map = "012"
        to_map = "0123456789"
        rv = self.rebase(str(n), from_map, to_map)
        return int(rv)


    # Stolen from: code.activestate.com
    # 496895-rebase-convert-a-number-tofrom-any-base-in-range-2
    # http://code.activestate.com/recipes/users/4173556/
    def rebase(self, number, from_alphabet, to_alphabet):
        if not isinstance(number, str):
            raise TypeError('The number must be a string.')

        if len(from_alphabet) < 2 or len(to_alphabet) < 2:
            raise ValueError('Alphabets must have at least two symbols.')
        if (sorted(set(from_alphabet)) != sorted(from_alphabet) or
                sorted(set(to_alphabet)) != sorted(to_alphabet)):
            raise ValueError('Alphabets cannot have any repeated symbols.')

        to_base = len(to_alphabet)
        from_base = len(from_alphabet)
        denary_number = 0

        for i in range(len(number)):
            denary_number += (from_base ** i) * from_alphabet.index(number[-(1 + i)])

        arbitrary_base_number = ''

        while denary_number != 0:
            arbitrary_base_number = ''.join(
                [to_alphabet[denary_number % to_base],
                arbitrary_base_number]
                )
            denary_number //= to_base

        if arbitrary_base_number == '':
            return '0'
        else:
            return arbitrary_base_number


    def move(self, target_square, new_value):
        # The number of the square is one more than the index we have to change.
        target_square = target_square - 1
        if target_square < 0 or target_square > 8:
            raise ValueError("target square is out of range")
        board_state = list(self.board)
        board_state[target_square] = str(new_value)
        self.board = ''.join(board_state)


    def has_winner(self):
        winning_patterns = [
            [0,1,2], [0,4,8], [0,3,6], [1,4,7], [2,4,6], [2,5,8],
            [3,4,5], [6,7,8]
        ]
        state = list(self.board)
        for pattern in winning_patterns:
            if state[pattern[0]] == '0':
                continue
            if state[pattern[1]] == state[pattern[0]] and state[pattern[2]] == state[pattern[0]]:
                return state[pattern[0]]
        return False
