import weapons

class Player:
   def __init__(self) -> None:
      self.health = 20
      self.weapons = []
      self.items = []
      self.materials = {
         "sticks":0,
         "leaves":0,
         "coconuts":0,
         "rocks":0
      }
      self.equipped_weapon = weapons.Fists()
      self.current_location = None

   def move_north(self, map):
        new_location = map.north(self.current_location)
        if new_location:
            self.current_location = new_location
        else:
            print("You cannot go into the ocean!")

   def move_east(self, map):
      new_location = map.east(self.current_location)
      if new_location:
         self.current_location = new_location
      else:
         print("You cannot go into the ocean!")

   def move_south(self, map):
      new_location = map.south(self.current_location)
      if new_location:
         self.current_location = new_location
      else:
         print("You cannot go into the ocean!")

   def move_west(self, map):
      new_location = map.west(self.current_location)
      if new_location:
         self.current_location = new_location
      else:
         print("You cannot go into the ocean!")

   def display_inventory(self):
      print("You have:")
      for material in self.materials:
         print(" -- " + str(self.materials[material]) + " " + material)

   def collect(self, item, num):
      self.materials[item] += num
      print("You collected " + str(num) + " " + item + "!")