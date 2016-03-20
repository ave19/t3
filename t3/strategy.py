#
# Strategy
#

class Strategy(object):

    def __init__(self, *args, **kwargs):
        self._data = {}
        self.strategy_map = {}

    # Implement "move" given a board.
    # Implement a callback like thing.

    def register(self, name, strategy):
        if isinstance(strategy, Strategy):
            self.strategy_map[str(name)] = strategy


class ManualStrategy(Strategy):

        def move(self, board):
            pass
