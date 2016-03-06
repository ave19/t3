#
#
#

from t3.strategy import Strategy

class Player(object):

    foo = False

    def __init__(self, name="Player One", symbol='*', *args, **kwargs):
        self._data = {}
        self.name = name
        self.symbol = symbol
        self.strategy = None

    @property
    def name(self):
        return self._data['name']

    @name.setter
    def name(self, new_name):
        self._data['name'] = str(new_name)

    @property
    def symbol(self):
        return self._data['symbol']

    @symbol.setter
    def symbol(self, symbol='*'):
        self._data['symbol'] = symbol

    @property
    def strategy(self):
        return self._data['strategy']

    @strategy.setter
    def strategy(self, new_strategy):

        # You can be None.
        if new_strategy == None:
            self._data['stragegy'] = None
        elif type(new_strategy) is Strategy:
            self._data['stragegy'] = new_strategy
        else:
            raise ValueError("new strategy must be Strategy, not %s" %
                type(new_strategy)
                )

    def collect_move(self):
        return input("\n   %s, choose a square for %s: " % (self.name, self.symbol))
