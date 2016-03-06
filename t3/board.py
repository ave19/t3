#
# A representation of a tic tac toe board
#


class Board(object):

    min_board = 0
    max_board = 3 ** 9
    min_spot = 1
    max_spot = 9
    string_map = { '0': ' ', '1': 'X', '2': 'O' }

# =====================================================================

    def __init__(self, *args, **kwargs):
        self._data = {}
        self.reset_board()


    def __str__(self):
        rv = "%s|%s|%s\n-|-|-\n%s|%s|%s\n-|-|-\n%s|%s|%s" % (
            tuple([ self.string_map[x] for x in list(self.board) ])
            )
        return rv


# =====================================================================

    @property
    def b10(self):
        return self.convert_to_base10(self.board)

# =====================================================================

    @property
    def board(self):
        # we want the base 3
        return self._data['board']


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

# =====================================================================

    def list_empty_spots(self):
        empties = []
        state = list(self.board)
        for x in range(0, 9):
            if state[x] == '0':
                empties.append(x+1)
        return empties


    def show_empty_spots(self):
        fillers = []
        empties = self.list_empty_spots()
        for x in range(1, 10):
            if x in empties:
                fillers.append(x)
            else:
                fillers.append(' ')
        return "%s|%s|%s\n-|-|-\n%s|%s|%s\n-|-|-\n%s|%s|%s" % tuple(fillers)


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


    def move(self, target_square, symbol):
        # The number of the square is one more than the index we have to change.
        new_value = self.get_player_number_by_symbol(symbol)

        target_square = int(target_square)

        if target_square < self.min_spot:
            raise ValueError("target square is too low: %s < %s" %
                (target_square, self.min_spot)
                )

        if target_square > self.max_spot:
            raise ValueError("target square is too high: %s > %s" %
                (target_square, self.max_spot)
                )

        if not target_square in self.list_empty_spots():
            raise ValueError("target square is not empty")

        self.board = self.board[:target_square-1] \
            + new_value \
            + self.board[target_square:]


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


    def is_full(self):
        if '0' in self.board:
            return False
        return True


    def get_player_number_by_symbol(self, symbol):
        if not symbol in self.string_map.values():
            raise ValueError("No value %s in my symbols: %s" % (
                symbol, self.string_map.values()
            ))
        for (k,v) in self.string_map.iteritems():
            if symbol == v:
                return k
