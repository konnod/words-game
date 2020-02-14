import logging
from src.game.IGame import Game
from src.player.Bot import Bot
from src.player.ConsolePlayer import ConsolePlayer
from src.context.GameContext import GameContext
from src.Config import *
from src.error.LogicError import LogicError


class GameVsBot(Game):
    def __init__(self):
        self.__context = GameContext(CONTEXT_FILE_PATH, DICTIONARY_FILE_PATH)
        self.__bot = Bot(self.__context.get_dictionary())
        self.__player = ConsolePlayer()
        # todo: get current player from context
        logging.debug(f'Setting current player to "{self.__player}"')
        self.__current_player = self.__player
        self.__other_player = self.__bot

    def start(self):
        while True:

            logging.debug(f'Requesting {self.__current_player} a word '
                          f'starting on letter \'{self.__context.get_last_letter()}\'')
            word = self.__current_player.request_word(self.__context.get_last_letter())
            logging.debug(f'{self.__current_player} returned word "{word}"')
            try:
                self.__context.submit_word(word)
            except LogicError as e:
                logging.debug(f'Word "{word}" was not accepted by game: {str(e)}')
                self.__current_player.word_error(str(e))
                continue

            if not self.__other_player.notify_word(word):
                logging.debug(f'{self.__other_player} rejected word "{word}"')
                self.__current_player.word_refused()
                self.__context.refuse_last_word()
                continue
            logging.debug(f'{self.__other_player} accepted word "{word}"')

            logging.debug('End of the turn. Switching current player')
            self.__switch_current_player()

    def __switch_current_player(self):
        if self.__current_player == self.__bot:
            self.__current_player = self.__player
            self.__other_player = self.__bot
        else:
            self.__current_player = self.__bot
            self.__other_player = self.__player

        logging.debug(f'Current player is now "{self.__current_player}"')
