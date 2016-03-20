#
#
#

from t3.strategy import Strategy, ManualStrategy

class Player(object):

    foo = False

    def __init__(self, name="Player One", symbol='*', *args, **kwargs):
        self._data = {}
        self.name = name
        self.symbol = symbol
        self.strategy = ManualStrategy()

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
    def strategy(self, new_strategy=None):

        # You can be None.
        if new_strategy == None:
            self._data['strategy'] = None
        elif isinstance(new_strategy, Strategy):
            self._data['strategy'] = new_strategy
        else:
            raise ValueError("new strategy must be Strategy, not %s" %
                type(new_strategy)
                )


    def move(self, board):
        return self.strategy.move(board, name=self.name, symbol=self.symbol)

    def win(self):
        print "%s is happy." % self.name
        self.strategy.win()

    def lose(self):
        print "%s is sad." % self.name
        self.strategy.lose()

    def draw(self):
        print "%s has mixed emotions." % self.name
        self.strategy.draw()
