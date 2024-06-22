import monsters


class Location:
    def __init__(self, y, x) -> None:
        self.name = ""
        self.type = ""
        self.enemies = []
        self.actions = []
        self.collectables = []
        self.desc = ""
        self.x = x
        self.y = y

    # TODO: Display action func (need actions implemented)


class Beach(Location):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.name = "B"
        self.type = "beach"
        self.enemies = [monsters.Crab]
        self.desc = "sandy beach"
        self.actions = ["Collect"]
        self.collectables += ["sticks", "leaves", "coconuts"]


class Mountain(Location):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.name = "M"
        self.type = "mountain"
        self.enemies = []
        self.desc = "rocky mountain"
        self.actions = ["Collect"]
        self.collectables += ["rocks"]


class Center(Location):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.name = "F"
        self.type = "center"
        self.desc = "lush forest"
