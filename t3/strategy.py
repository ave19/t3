#
# Strategy
#
from abc import ABCMeta, abstractmethod, abstractproperty

class Strategy(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def move(self, board=None, *args, **kwargs):
        # Given a board, choose a move.
        pass

    @abstractmethod
    def win(self, board=None, *args, **kwargs):
        # Do something if you win.
        pass

    @abstractmethod
    def lose(self, board=None, *args, **kwargs):
        # Do something if you lose.
        pass

    @abstractmethod
    def draw(self, board=None, *args, **kwargs):
        # Do something if you tie/draw.
        pass


class TestStrategy(Strategy):

    def move(self, board=None):
        # Always picks 1
        return 1
    def win(self):
        # Test 2
        pass
    def lose(self):
        pass
    def draw(self):
        pass


class ManualStrategy(Strategy):

    def __init__(self, *args, **kwargs):
        self._data = {}
        self.strategy_map = {}

    def move(self, board, *args, **kwargs):
        name = kwargs.get("name", "RandomPlayer")
        symbol = kwargs.get("symbol", "#")
        print "\nThe Board: (%s)\n%s" % (board.b10, board)
        print "\nAvailable Moves:\n%s" % board.show_empty_spots()
        return input("\n   %s, choose a square for %s: " % (name, symbol))

    def win(self, board=None):
        print "I won!"

    def lose(self, board=None):
        #print "I lost!"
        pass
    def draw(self, board=None):
        #print "I almost won!"
        pass
