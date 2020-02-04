import abc


class Player(abc.ABC):
    """
    Requests the word from player starting with @letter
    """
    @abc.abstractmethod
    def request_word(self, letter: str) -> str:
        pass

    """
    Is called when game refuses players word
    """
    @abc.abstractmethod
    def refuse_word(self):
        pass

    """
    Notifies player about work from other player
    Returns True if player accepts other player word and False if refuses
    """
    @abc.abstractmethod
    def notify_word(self, word: str) -> bool:
        pass
