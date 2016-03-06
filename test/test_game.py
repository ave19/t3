import unittest
from t3.game import Game

class test_game(unittest.TestCase):

    g = None

    def setUp(self):
        self.g = Game()

    def test_class(self):
        self.assertIsInstance(self.g, Game, "s is not Game")



if __name__ == '__main__':
    unittest.main()
