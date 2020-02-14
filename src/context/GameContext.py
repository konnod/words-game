import logging
from os import path
from src.context.IContext import Context
from src.error.LogicError import LogicError
from src.context.dictionary.FileDictionary import FileDictionary


class GameContext(Context):

    def __init__(self, saved_path: str, dictionary_path: str):
        self.__saved_path = saved_path

        # create file if not exists
        if not path.exists(self.__saved_path):
            logging.debug('Save file does not exist, creating')
            open(self.__saved_path, 'x').close()

        # load used words
        try:
            with open(self.__saved_path, mode='r') as file:
                self.__used_words = file.read().split('\n')
        except IOError:
            logging.error('Failed to open save file for reading')
            raise Exception('Failed to open save file for reading')
        logging.debug('Successfully read last game')

        # check last word to be not empty - to prevent bugs
        if len(self.__used_words[-1]) == 0:
            self.__used_words.pop()

        logging.debug(f'Words already used: {len(self.__used_words)}')

        # get last letter
        if len(self.__used_words) == 0:
            self.__last_letter = ''
        else:
            self.__last_letter = self.__used_words[-1][-1]

        logging.debug(f'Last letter is {self.__last_letter}')

        # get letter before last
        if len(self.__used_words) <= 1:
            self.__prev_letter = ''
        else:
            self.__prev_letter = self.__used_words[-2][-1]

        self.__dictionary = FileDictionary(dictionary_path, set(self.__used_words))

    def submit_word(self, word: str):
        # check word to actually start with last letter
        if not word.lower().startswith(self.__last_letter):
            logging.error("Word does not start with last letter")
            raise LogicError('Word does not start with last letter')

        if word in self.__used_words:
            logging.error("Word already used")
            raise LogicError('Word already used')

        # validate word to be in dictionary
        if not self.__dictionary.contains(word):
            logging.error("Word is absent in dictionary")
            raise LogicError('Word is absent in dictionary')

        # update used words
        self.__used_words.append(word)

        # update dictionary
        self.__dictionary.remove_word(word)

        # update prev letter
        self.__prev_letter = self.__last_letter

        # update last letter
        self.__last_letter = word[-1]

        # save word to file
        self.__save_used_word(word)

    def refuse_last_word(self):
        # Here we don't modify neither dictionary nor used words,
        # last word becomes used and absent in dictionary.
        # Moreover, it will not appear in dictionary when game will resume
        # So we only update last letter
        self.__last_letter = self.__prev_letter

    def get_last_letter(self):
        return self.__last_letter

    def get_dictionary(self):
        return self.__dictionary

    def __save_used_word(self, word: str):
        logging.debug(f'Saving word "{word}" to save file')
        try:
            with open(self.__saved_path, mode='a+') as file:
                file.writelines("%s\n" % word)
        except IOError:
            logging.error('Failed to write save to file')
            raise Exception('Failed to write save to file')
