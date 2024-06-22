import location


class Map:
    def __init__(self) -> None:
        self.locations = []

    def display(self):
        print()
        for row in self.map:
            for loc in row:
                print("[" + loc.name + "]", end="")
            print()
        print()

    def north(self, location):
        if location.y > 0:
            return self.locations[location.y - 1][location.x]
        return False

    def east(self, location):
        if location.x < len(self.locations[location.y]) - 1:
            return self.locations[location.y][location.x + 1]
        return False

    def south(self, location):
        if location.y < len(self.locations) - 1:
            return self.locations[location.y + 1][location.x]
        return False

    def west(self, location):
        if location.x > 0:
            return self.locations[location.y][location.x - 1]
        return False


class IslandMap(Map):
    def __init__(self) -> None:
        super().__init__()
        self.locations = [[location.Mountain(0, 0), location.Mountain(0, 1), location.Mountain(0, 2)],
                          [location.Mountain(1, 0), location.Center(1, 1), location.Beach(1, 2)],
                          [location.Beach(2, 0), location.Beach(2, 1), location.Beach(2, 2)]]
