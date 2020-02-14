import abc


class Context(abc.ABC):

    @abc.abstractmethod
    def submit_word(self, word: str) -> bool:
        pass

    @abc.abstractmethod
    def refuse_last_word(self):
        pass

    @abc.abstractmethod
    def get_last_letter(self):
        pass

    @abc.abstractmethod
    def get_dictionary(self):
        pass
