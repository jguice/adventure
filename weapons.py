import attack


class Weapon:
    def __init__(self) -> None:
        self.attacks = []

    def display_info(self):
        """Display function with full attack info"""
        for move in self.attacks:
            print(move.name + ":")
            print("  Accuracy: " + str(move.accuracy))
            print("  Damage: " + str(move.damage))
            print("  Number of attacks: " + str(move.attack_num))

    def display(self):
        """Display function for menus"""
        count = 1
        for move in self.attacks:
            print(str(count) + ". " + move.name)
            count += 1


class Fists(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.attacks = [attack.FlurryPunch(), attack.SuckerPunch()]
