import attack
import dice as d

dice = d.Dice()


class Monster:
    def __init__(self) -> None:
        self.name = ""
        self.health = 0
        self.attacklist = []
        self.num_attacks = 0

    def select_move(self):
        """Selects a move at random"""
        move = dice.custom(self.num_attacks)
        return self.attacklist[move - 1]


class Crab(Monster):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Crab"
        self.health = 6
        self.attacklist = [attack.Snip()]
        self.num_attacks = 1
