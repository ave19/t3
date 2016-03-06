import unittest
from t3.player import Player

class test_player(unittest.TestCase):

    p = None

    def setUp(self):
        self.p = Player()

    def test_class(self):
        self.assertIsInstance(self.p, Player, "p is not Player")

    def test_init_with_name(self):
        expected = "foo"
        p = Player(expected)
        self.assertEqual(p.name, expected, "name isn't foo")



if __name__ == '__main__':
    unittest.main()
