import os.path
import logging
from random import seed
from random import randint
from src.context.dictionary.Dictionary import IDictionary
from src.error.LogicError import LogicError


class FileDictionary(IDictionary):

    def __init__(self, dict_path: str, used_words: set = None):

        seed(1)

        if not os.path.isfile(dict_path):
            logging.error('Dictionary file does not exist')
            raise Exception('Dictionary file does not exist')

        try:
            with open(dict_path) as file:
                self.__dictionary = set(file.read().split('\n'))
        except IOError:
            logging.error('Failed to open dictionary file')
            raise Exception('Failed to open dictionary file')
        logging.debug('Successfully opened dictionary file!')

        # check dictionary not to be empty
        if len(self.__dictionary) == 0:
            logging.error('Dictionary is empty')
            raise Exception('Dictionary is empty')

        # remove used words from dictionary - difference
        if used_words is not None:
            self.__dictionary = self.__dictionary - used_words

        logging.debug(f'Dictionary contains {len(self.__dictionary)} words in use')

    def contains(self, word: str) -> bool:
        return word in self.__dictionary

    def get_word(self, letter: str) -> str:
        if len(letter) > 1 or not letter.isalpha():
            logging.error('First letter to get a word from dictionary is invalid:', letter)
            raise LogicError('First letter to get a word from dictionary is invalid')

        possible_words = [word for word in self.__dictionary if word.lower().startswith(letter.lower())]
        word = possible_words[randint(0, len(possible_words) - 1)]
        logging.debug(f'Word {word} is fetched from dictionary')
        return word

    def remove_word(self, word: str):
        self.__dictionary.remove(word)
        logging.debug(f'Word {word} is removed from dictionary')
