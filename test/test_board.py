import unittest
from board import Board

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
        
        
if __name__ == '__main__':
    unittest.main()