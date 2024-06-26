# 🗡️ Adventure! 🗡️

A text-based adventure where you roam a map, battle monsters, and craft a variety of items.

## Prerequisites

- Python

## How to Run

`python main.py`

## Development

### Documentation

#### [docstring](https://peps.python.org/pep-0257/) documentation

To view docstring style documentation:

1. Install [pdoc](https://pdoc.dev)
2. Run `pdoc *.py` in the project root, then visit http://localhost:8080

#### diagrams

##### Class Diagram

This diagram uses [mermaid](https://mermaid.live) for rendering.

```mermaid
classDiagram
    class Attack {
        - name: str
        - damage: int
        - accuracy: int
        - attack_num: int
    }

    class Snip {
        + __init__()
    }

    class FlurryPunch {
        + __init__()
    }

    class SuckerPunch {
        + __init__()
    }

    Attack <|-- Snip: is a
    Attack <|-- FlurryPunch: is a
    Attack <|-- SuckerPunch: is a
%% ------------------------------------

    class Battle {
        - moveslist: list
        - monster: Monster
        - player: Player
        + __init__(player, monster)
        + display_moves()
        + run()
        + accuracy_check(attack)
        + monster_attack()
        + player_attack()
        + attack_cycle()
        + battle_cycle()
    }

    Battle --* Player: has a
    Battle --* Monster: has a
    Battle --* Dice: uses
%% ------------------------------------

    class Location {
        - name: str
        - type: str
        - desc: str
        - enemies: list
        - actions: list
        - collectables: list
    }

    class Beach {
        + __init__(x, y)
    }

    class Mountain {
        + __init__(x, y)
    }

    class Center {
        + __init__(x, y)
    }

    Location <|-- Beach: is a
    Location <|-- Mountain: is a
    Location <|-- Center: is a
    Location --* Monster: has 1 or more
%% ------------------------------------

    class Weapon {
        - attacks: list
        + display_info()
        + display()
    }

    class Fists {
        + __init__()
    }

    Weapon <|-- Fists: is a
    Weapon --> Attack: has 1 or more
%% ------------------------------------

    class Monster {
        - name: str
        - health: int
        - attacklist: list
        - num_attacks: int
        + select_move()
    }

    class Crab {
        + __init__()
    }

    Monster <|-- Crab: is a
    Monster --> Attack: has 1 or more
    Monster --* Dice: uses
%% ------------------------------------

    class Item {
        - name: str
        - recipe: dict
        - type: str
    }

    class CrudePickaxe {
        - subtype: str
        + __init__()
    }

    Item <|-- CrudePickaxe: is a
%% ------------------------------------

    class Map {
        - locations: list
        + __init__()
        + display()
        + north(Location)
        + east(Location)
        + south(Location)
        + west(Location)
    }

    class IslandMap {
        + __init__()
    }

    Map <|-- IslandMap: is a
    Map --* Location: has 1 or more
%% ------------------------------------

    class Player {
        - health: int
        - weapons: list
        - items: list
        - materials: dict
        - equipped_weapon: Item
        - current_location: Location
        + __init__()
        + move_north(Map)
        + move_east(Map)
        + move_south(Map)
        + move_west(Map)
        + display_inventory()
        + collect(Item, num)
    }

    Player --* Location: has a
    Player --* Item: has 1 or more
    Player --* Weapon: has 1 or more

    class Dice {
        + __init__()
        + d2()
        + custom(int)
        + d100()
    }

    class Game {
        - player: Player
        - current_map: Map
        - island_map: Map
        - dice: Dice
        - actions_list: List[Action]
        + __init__()
        + display_island_map()
        + move()
        + action_display()
        + action_select()
        + collect_select()
        + action()
        + gameloop()
    }

    Game --* Player: has a
    Game --* Map: has a
    Game --* Dice: uses
    Game --* Battle: uses
```

