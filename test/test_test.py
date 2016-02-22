import unittest


class test_test(unittest.TestCase):

    context = None

    def setUp(self):
        self.context = True

    def test_true(self):
        self.failUnless(True)

    def test_context(self):
        self.failUnless(self.context)


if __name__ == '__main__':
    unittest.main()
