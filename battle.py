import dice as d

dice = d.Dice()


class Battle:
    def __init__(self, player, monster) -> None:
        self.moveslist = "Attack", "Run"
        self.monster = monster
        self.player = player

    def display_moves(self):
        """Displays moves
        TODO: Move moveslist into player object"""
        print("Available actions:")
        for move in self.moveslist:
            print("- " + move + " (" + move[0].lower() + ")")
        print()

    def run(self):
        """Run action in battle loop
        TODO: Add speed stat comparison instead of coin flip"""
        if dice.d2() == 1:
            print("Couldn't escape!")
            return False
        else:
            print("You escaped!")
            return True

    def accuracy_check(self, attack):
        """Compares the accuracy of a given move to a d100 to see if it hits"""
        if dice.d100() <= attack.accuracy:
            return True
        else:
            return False

    def monster_attack(self):
        """Controls monster attacks during battle sequence"""
        # selects a random move from the monster's attack list
        move = self.monster.attacklist[dice.custom(self.monster.num_attacks) - 1]
        # if the attack hits, player takes damage, otherwise lets player know it missed
        if self.accuracy_check(move):
            self.player.health -= move.damage
            print("You took " + str(move.damage) + " damage from " + self.monster.name + "!")
        else:
            print("Enemy " + self.monster.name + " missed!")

    def player_attack(self):
        """Controls player attack input and logic
        TODO: Maybe split into two functions?"""
        # shortcut for self.player.equipped_weapon because it's used a lot here
        weapon = self.player.equipped_weapon

        # in while loop for error checking purposes
        while True:
            weapon.display()
            command = input("What attack would you like to use? (Enter 'i' for more info): ")
            # attempts to use numbered attack from input
            try:
                if (int(command) - 1) <= len(weapon.attacks):
                    # shortcuts selected attack to attack
                    attack = weapon.attacks[int(command) - 1]
                    # repeats process for num_attacks stat
                    for hit in range(1, attack.attack_num + 1):
                        # if hits, lets player know attack hit and same for miss
                        if self.accuracy_check(attack):
                            print("Attack " + str(hit) + " hit!")
                            self.monster.health -= attack.damage
                        else:
                            print("Attack " + str(hit) + " missed!")
                    break
                # if inputted number is out of range, returns error message
                else:
                    print("I don't understand!")
            # if input is not a number, checks if player wants info then returns error
            except:
                if command in ['i', 'info']:
                    weapon.display_info()
                else:
                    print("I don't understand!")

    def attack_cycle(self):
        """Controls 'attack' action"""
        while self.monster.health > 0:
            print("Your health is: " + str(self.player.health))
            self.player_attack()
            if self.monster.health > 0:
                self.monster_attack()
        print(self.monster.name + " defeated!")

    def battle_cycle(self):
        """Controls entire battle
        TODO: Move actions to be attributes of player? Currently hardcoded (no new actions as game progeresses)"""
        print("\nYou encounterd a " + self.monster.name + "!\n")
        while True:
            self.display_moves()
            command = input("What would you like to do?: ").lower()
            if command in ["run", "r"]:
                if self.run():
                    break
                else:
                    self.monster_attack()
            elif command in ["attack", "a"]:
                self.attack_cycle()
                break
            else:
                print("I don't understand!")
