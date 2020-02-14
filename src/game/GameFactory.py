import logging
from src.game.GameVsBot import GameVsBot
from src.Config import *
from src.error.LogicError import LogicError


class GameFactory:

    @staticmethod
    def create_game():
        # if GAME_VS_BOT:
        logging.debug('Creating game vs bot')
        return GameVsBot()
        # else:
        #     logging.error('Game vs player is not implemented')
        #     raise LogicError("Game vs player not implemented")
