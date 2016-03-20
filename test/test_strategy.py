import unittest
from t3.strategy import Strategy, TestStrategy

class test_strategy(unittest.TestCase):

    s = None

    def setUp(self):
        # Strategy is an abstract base class, it cannot be instantiated.
        self.s = TestStrategy()

    def test_class(self):
        self.assertIsInstance(self.s, Strategy, "s is not Strategy")

    def test_the_test(self):
        expected = 1
        self.assertEqual(expected, self.s.move())


if __name__ == '__main__':
    unittest.main()
