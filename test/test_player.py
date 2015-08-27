import unittest
from t3.player import Player

class test_player(unittest.TestCase):
    
    p = None
    
    def setUp(self):
        self.p = Player()
        
        
        
if __name__ == '__main__':
    unittest.main()