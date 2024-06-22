class Item:
    def __init__(self) -> None:
        self.name = ""
        self.recipe = {}
        self.type = ""


class CrudePickaxe(Item):
    def __init__(self) -> None:
        self.name = "Crude Pickaxe"
        self.recipe = {
            "sticks": 3,
            "rocks": 5,
            "leaves": 5,
        }
        self.type = "item"
        self.subtype = "pickaxe"
