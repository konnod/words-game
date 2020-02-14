import abc


class IDictionary(abc.ABC):

    @abc.abstractmethod
    def contains(self, word: str) -> bool:
        pass

    @abc.abstractmethod
    def get_word(self, letter: str) -> str:
        pass

    @abc.abstractmethod
    def remove_word(self, word: str):
        pass
