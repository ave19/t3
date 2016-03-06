import unittest
from t3.strategy import Strategy

class test_strategy(unittest.TestCase):

    s = None

    def setUp(self):
        self.s = Strategy()

    def test_class(self):
        self.assertIsInstance(self.s, Strategy, "s is not Strategy")



if __name__ == '__main__':
    unittest.main()
