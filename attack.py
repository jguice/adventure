"""Attacks module

This module defines attacks available in the game.
"""


class Attack:
    """Attack base class

    Contains properties and methods common to all attacks.

    """
    name: str
    "name of the attack"
    damage: int
    "hp damage inflicted by the attack"
    accuracy: int
    "attack accuracy as a percentage"
    attack_num: int
    "number of times attack fires per event"


class Snip(Attack):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Snip"
        self.damage = 3
        self.accuracy = 70
        self.attack_num = 1


class FlurryPunch(Attack):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flurry Punch"
        self.damage = 2
        self.accuracy = 70
        self.attack_num = 2


class SuckerPunch(Attack):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Sucker Punch"
        self.damage = 3
        self.accuracy = 90
        self.attack_num = 1
