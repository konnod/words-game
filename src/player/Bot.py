from src.player.IPlayer import Player
from src.context.dictionary.Dictionary import IDictionary


class Bot(Player):

    def __init__(self, dictionary: IDictionary):
        self.__dictionary = dictionary

    def request_word(self, letter: str) -> str:
        return self.__dictionary.get_word(letter)

    def word_error(self, err: str):
        pass

    def word_refused(self):
        pass

    def notify_word(self, word: str) -> bool:
        return True

    def __str__(self):
        return "Bot"
