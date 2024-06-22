import random


class Dice:
    def __init__(self) -> None:
        pass

    def d2(self):
        """Flip a coin"""
        return random.randint(1, 2)

    def custom(self, top):
        """Make your own dice!!"""
        return random.randint(1, top)

    def d100(self):
        """Random number 1-100"""
        return random.randint(1, 100)
