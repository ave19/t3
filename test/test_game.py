import unittest
from t3.game import Game

class test_game_init(unittest.TestCase):

    g = None

    def setUp(self):
        self.g = Game()

    def test_class(self):
        self.assertIsInstance(self.g, Game, "s is not Game")


# class test_game_interaction(unittest.TestCase):
#
#     g = None
#
#     def setUp(self):
#         self.g = Game()
#         self.g.board.board = self.g.board.convert_to_base3(8586)
#         print "the board: " % self.g.board
#
#     def test_a_move(self):
#         #self.g.play()
#         pass


if __name__ == '__main__':
    unittest.main()
