from Chatbot import Chatbot
import json
import random

# This code block allows relative imports from a directory path
import sys
byu_eve_path = "../../byu_eve/byu_eve"  # TODO: change this path!!!!
sys.path.append(byu_eve_path)
import byu_eve
from byu_eve.characters.Don_Quarlos import DonQuarlos


class DonQuarlosBot(Chatbot):
    def __init__(self, verbose=False):
        self.name = "Don Quarlos"
        self.message = "Hello, how are you?"
        self.bot = DonQuarlos(verbose)
        self.verbose = verbose
        super(DonQuarlosBot, self).__init__(graph=self.bot.kg)

    def send_message(self):
        possible_messages = self.bot.response(self.message)
        # pick a random answer from the top 3, get the text part
        self.message = random.choice(possible_messages[:3])[0]
        return {"text": f"{self.name}->Plr: {self.message}"}

    def recv_message(self, message):
        self.message = message
        return super().recv_message(message)


# just for testing
if __name__ == "__main__":
    bot = DonQuarlosBot()
    print("Plr->Don Quarlos: Hello, how are you?")
    print(bot.send_message()["text"])
    print("Plr->Don Quarlos: ", end="")
    bot.recv_message(input())
    print(bot.send_message()["text"])

