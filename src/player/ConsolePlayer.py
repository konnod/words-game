from src.player.IPlayer import Player


class ConsolePlayer(Player):

    def request_word(self, letter: str) -> str:

        if len(letter) == 0:
            print("You're lucky, your turn is first!")
            print("Print any word!")
        else:
            print("Print word starting on letter ", letter)

        print("(Game expects you to not invent one, so be careful)")
        print(">>> ", end='')
        word = str(input())
        print("\n")

        return word

    def word_error(self, err: str):
        print("I said you to be careful!")
        print("Game does not accept your word...")
        print("You've received an error: \"", err, "\"")
        print("Keep your eyes and mind open, just concentrate and provide another one")
        print("\n")

    def word_refused(self):
        print("Another player has refused your word!")
        print("What a son of a bitch!")
        print("\n")

    def notify_word(self, word: str) -> bool:
        print("Another player has made his turn!")
        print("The word is \"",word,"\"")
        print("Do you accept this word?")
        print("print \"no\" if you don't or any otherwise")
        print(">>> ")
        res = str(input())
        print("\n")

        if res == "no" or res == "n":
            return False

        return True

    def __str__(self):
        return "Console player"
