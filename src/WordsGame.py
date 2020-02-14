import sys
import traceback
import logging
from src.game.GameFactory import GameFactory


def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename='words-game.log',
                        level=logging.DEBUG)
    logging.debug('\n\n')
    logging.debug('*****************************************')
    logging.debug('Creating game')
    try:
        game = GameFactory.create_game()
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        traceback.print_exc()
        sys.exit(127)

    logging.debug('Game init successful. Starting game')

    game.start()


main()
