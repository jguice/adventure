import battle
import dice
import player
import map


class Game:
    def __init__(self) -> None:
        self.player = player.Player()
        self.island_map = map.IslandMap()
        self.current_map = self.island_map
        self.player.current_location = self.island_map.locations[1][1]
        self.dice = dice.Dice()
        self.actions_list = ["Collect items"]

    def display_island_map(self):
        print()
        for row in self.island_map.locations:
            for loc in row:
                if loc == self.player.current_location:
                    print("[+]", end="")
                else:
                    print("[" + loc.name + "]", end="")
            print()
        print()

    def move(self, command):
        if command == "w":
            self.player.move_north(self.current_map)
            self.display_island_map()
        elif command == "d":
            self.player.move_east(self.current_map)
            self.display_island_map()
        elif command == "s":
            self.player.move_south(self.current_map)
            self.display_island_map()
        elif command == "a":
            self.player.move_west(self.current_map)
            self.display_island_map()
        print("You are now in a " + self.player.current_location.desc + "\n")

    def action_display(self):
        count = 0
        print("Available actions:")
        print("--WASD to move, Q to quit, I to view inventory")
        for action in self.player.current_location.actions:
            count += 1
            print(str(count) + ". " + action)

    def action_select(self):
        while True:
            actions = self.player.current_location.actions
            self.action_display()
            command = input("What would you like to do?: ")
            try:
                if (int(command) - 1) <= len(actions):
                    return actions[int(command) - 1]
                # if inputted number is out of range, returns error message
                else:
                    print("I don't understand! (OOR)")
                # if input is not a number, checks if player wants info then returns error
            except:
                if command in ['w', 'a', 's', 'd']:
                    self.move(command)
                elif command.lower() in ['quit', 'q']:
                    exit()
                elif command.lower() in ['inventory', 'i']:
                    self.player.display_inventory()
                else:
                    print("I don't understand! (NAN)")

    def collect_select(self):
        while (True):
            count = 1
            collectables = self.player.current_location.collectables
            for collectable in collectables:
                print(str(count) + ". Collect " + collectable)
                count += 1
            command = input("What would you like to collect?: ")
            try:
                if (int(command) - 1) <= len(collectables):
                    self.player.collect(collectables[int(command) - 1], 2)
                    break
                # if inputted number is out of range, returns error message
                else:
                    print("I don't understand! (OOR)")
                # if input is not a number, checks if player wants info then returns error
            except:
                print("I don't understand! (NAN)")

    def action(self):
        command = self.action_select()
        if self.dice.d2() == 1 and self.player.current_location.enemies:
            battle.Battle(self.player, self.player.current_location.enemies[
                self.dice.custom(len(self.player.current_location.enemies)) - 1]()).battle_cycle()
        if command == "Collect":
            self.collect_select()
        self.display_island_map()
        print("You are now in a " + self.player.current_location.desc + ".")
        print()

    def gameloop(self):
        print("You wake up stranded on a mysterious island in a " + self.player.current_location.desc + "...")
        self.display_island_map()
        print()
        while True:
            self.action()
