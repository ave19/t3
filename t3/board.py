#
# A representation of a tic tac toe board
#


class Board(object):

    min_board = 0
    max_board = 3 ** 9

    def __init__(self, *args, **kwargs):
        self._data = {}

    def __str__(self):
        base3_board = self.convert_to_base3(self.board)
        string_map = {
            '0': ' ',
            '1': 'X',
            '2': 'O'
        }

        rv = "%s|%s|%s\n-|-|-\n%s|%s|%s\n-|-|-\n%s|%s|%s" % (
                string_map[base3_board[0]],
                string_map[base3_board[1]],
                string_map[base3_board[2]],
                string_map[base3_board[3]],
                string_map[base3_board[4]],
                string_map[base3_board[5]],
                string_map[base3_board[6]],
                string_map[base3_board[7]],
                string_map[base3_board[8]]
            )
        return rv

    @property
    def board(self):
        # we want the base 3
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

    def convert_to_base3(self, n, base=3):
        from_map = "0123456789"
        to_map = "012"
        rv = self.rebase(str(n), from_map, to_map)
        # print "convert to base3: %s --> %s" % (n, rv)
        return rv.zfill(9)

    def convert_to_base10(self, n, base=3):
        from_map = "012"
        to_map = "0123456789"
        rv = self.rebase(str(n), from_map, to_map)
        # print "convert to base3: %s --> %s" % (n, rv)
        return rv.zfill(9)

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
            arbitrary_base_number = ''.join([to_alphabet[denary_number % to_base], arbitrary_base_number])
            denary_number //= to_base

        return arbitrary_base_number


    def move(self, target_square):
        if target_square < 0 or target_square > 9:
            raise ValueError("target square is out of range")
        this_board = self.convert_to_base3(self.board)
        print "this_board: %s" % this_board
