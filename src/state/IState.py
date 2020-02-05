import abc


class State(abc.ABC):

    @abc.abstractmethod
    def validate_word(self, word: str) -> bool:
        pass

    @abc.abstractmethod
    def refuse_last_word(self):
        pass
