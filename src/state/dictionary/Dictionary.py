import abc


class Dictionary(abc.ABC):

    @abc.abstractmethod
    def contains(self, word: str) -> bool:
        pass
