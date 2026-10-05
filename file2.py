from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch", sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        print("Sender:", self._sender)
        print("Recipient:", self._recipient)
        print("Happy birthday")
        print("Sender's age:", self._sender_age)