import unittest
from t3.board import Board


class test_player(unittest.TestCase):

    p = None

    def setUp(self):
        self.b = Board()

    def test_class(self):
        self.assertIsInstance(self.b, Board, "b is not Board")

    def test_board_set(self):
        expected = 4
        self.b.board = expected
        self.assertEqual(self.b.board, expected, "Board is not expected value")

    def test_board_set_too_low(self):
        too_low = self.b.min_board - 1
        with self.assertRaises(ValueError):
            self.b.board = too_low

    def test_board_set_too_high(self):
        too_high = self.b.max_board + 1
        with self.assertRaises(ValueError):
            self.b.board = too_high

    def test_convert_to_string(self):
        self.b.board = 12345
        expected = "121221020"
        self.assertEqual(self.b.convert_to_base3(self.b.board), expected)

#
# Empty Board Tests
#
    def test_convert_to_string_empty(self):
        self.b.board = 0
        expected = "000000000"
        self.assertEqual(self.b.convert_to_base3(self.b.board), expected)

    def test_board_as_string_empty(self):
        self.b.board = 0
        expected = " | | \n-|-|-\n | | \n-|-|-\n | | "
        self.assertEqual(str(self.b), expected)

    def test_convert_to_string_8000(self):
        self.b.board = 8000
        expected = "101222022"
        self.assertEqual(self.b.convert_to_base3(self.b.board), expected)


#
# Center Square Tests
#
    def test_convert_to_string_center_square(self):
        self.b.board = 81
        expected = "000010000"
        self.assertEqual(self.b.convert_to_base3(self.b.board), expected)

    def test_board_as_string_center_square(self):
        self.b.board = 81
        expected = " | | \n-|-|-\n |X| \n-|-|-\n | | "
        self.assertEqual(str(self.b), expected)

#
# Rebase Tests
#
    def test_rebase_hex(self):
        test_number = "B"
        expected = "11"
        from_a = "0123456789ABCDEF"
        to_a = "0123456789"
        self.assertEqual(self.b.rebase(test_number, from_a, to_a), expected)

    def test_simple_rebase_to_base3(self):
        test_number = "1"
        expected = "1"
        from_a = "0123456789"
        to_a = "012"
        self.assertEqual(self.b.rebase(test_number, from_a, to_a), expected)

    def test_simple_rebase_to_base10(self):
        test_number = "10020120"
        expected = "2364"
        to_a = "0123456789"
        from_a = "012"
        self.assertEqual(self.b.rebase(test_number, from_a, to_a), expected)

#
# Moves
#
    def test_move_set_too_low(self):
        move = -1
        with self.assertRaises(ValueError):
            self.b.move(move)


if __name__ == '__main__':
    unittest.main()
