import abc


class Game(abc.ABC):

    """
    Starts the game
    """
    @abc.abstractmethod
    def start(self):
        pass
