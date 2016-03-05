import unittest
from t3.board import Board


class test_player(unittest.TestCase):

    p = None

    def setUp(self):
        self.b = Board()

    def test_class(self):
        self.assertIsInstance(self.b, Board, "b is not Board")

    def test_set_board(self):
        expected = '000111222'
        self.b.board = expected
        self.assertEqual(self.b.board, expected, "board value not set correctly")

    def test_reset_board(self):
        expected = '000000000'
        self.b.board = '111222111'
        self.b.reset_board()
        self.assertEqual(self.b.board, expected, "board did not reset")

    def test_string_display(self):
        expected = " | | \n-|-|-\nX|X|X\n-|-|-\nO|O|O"
        self.b.board = '000111222'
        self.assertEqual(str(self.b), expected, "not the right board")

    def test_move_int(self):
        self.b.board = '000000000'
        self.b.move(5, 1)
        expected = '000010000'
        self.assertEqual(self.b.board, expected, "didn't move right")

    def test_move_str(self):
        self.b.board = '000000000'
        self.b.move(5, '1')
        expected = '000010000'
        self.assertEqual(self.b.board, expected, "didn't move right")

    def test_square_one_is_upper_right(self):
        expected = "X| | \n-|-|-\n | | \n-|-|-\n | | "
        self.b.board = '000000000'
        self.b.move(1, '1')
        self.assertEqual(str(self.b), expected, "square one not upper right")

    def test_convert_to_base10(self):
        expected = 8038
        self.b.board = '102000201'
        self.assertEqual(self.b.b10, expected,
            "failed to convert to base 10: %s != %s" % (expected, self.b.b10)
            )

    def test_winner_top_row(self):
        self.b.board = '111020002'
        self.assertEqual(self.b.has_winner(), '1')
        expected = 'X|X|X\n-|-|-\n |O| \n-|-|-\n | |O'
        self.assertEqual(str(self.b), expected)

    def test_winner_middle_row(self):
        self.b.board = '101222010'
        self.assertEqual(self.b.has_winner(), '2')

    def test_winner_bottom_row(self):
        self.b.board = '202200111'
        self.assertEqual(self.b.has_winner(), '1')

    def test_winner_left_col(self):
        self.b.board = '100120102'
        self.assertEqual(self.b.has_winner(), '1')

    def test_winner_center_col(self):
        self.b.board = '012010210'
        self.assertEqual(self.b.has_winner(), '1')
        expected = ' |X|O\n-|-|-\n |X| \n-|-|-\nO|X| '
        self.assertEqual(str(self.b), expected)

    def test_winner_right_col(self):
        self.b.board = '001021201'
        self.assertEqual(self.b.has_winner(), '1')
        expected = ' | |X\n-|-|-\n |O|X\n-|-|-\nO| |X'
        self.assertEqual(str(self.b), expected)

    def test_winner_diag_one_to_nine(self):
        self.b.board = '100210201'
        self.assertEqual(self.b.has_winner(), '1')

    def test_winner_diag_three_to_seven(self):
        self.b.board = '001212100'
        self.assertEqual(self.b.has_winner(), '1')

    def test_board_as_string_empty(self):
        self.b.board = '000000000'
        expected = " | | \n-|-|-\n | | \n-|-|-\n | | "
        self.assertEqual(str(self.b), expected)

    def test_board_display(self):
        self.b.board = '100200100'
        expected = 'X| | \n-|-|-\nO| | \n-|-|-\nX| | '
        self.assertEqual(str(self.b), expected)

    def test_board_one_is_top_left(self):
        self.b.board = '100000000'
        expected = "X| | \n-|-|-\n | | \n-|-|-\n | | "
        self.assertEqual(str(self.b), expected)

#
# Rebase Tests
#
    def test_convert_board_to_base10(self):
        self.b.board = '000111222'
        expected = 377
        self.assertEqual(self.b.b10, expected)

    def test_convert_number_to_board(self):
        number = 12345
        expected = '121221020'
        self.assertEqual(self.b.convert_to_base3(number), expected)

    def test_81_is_x_in_center_square(self):
        number = 81
        expected = '000010000'
        self.assertEqual(self.b.convert_to_base3(number), expected)

#
# Moves
# #
#     def test_move_set_too_low(self):
#         move = -1
#         with self.assertRaises(ValueError):
#             self.b.move(move)


if __name__ == '__main__':
    unittest.main()
