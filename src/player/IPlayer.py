import abc


class Player(abc.ABC):
    """
    Requests the word from player starting with @letter
    """
    @abc.abstractmethod
    def request_word(self, letter: str) -> str:
        pass

    """
    Is called when word returned from @request_word is invalid
    """
    @abc.abstractmethod
    def word_error(self, err: str):
        pass

    """
    Is called when game refuses players word
    """
    @abc.abstractmethod
    def word_refused(self):
        pass

    """
    Notifies player about word from other player
    Must return True if player accepts other player word and False if refuses
    """
    @abc.abstractmethod
    def notify_word(self, word: str) -> bool:
        pass
