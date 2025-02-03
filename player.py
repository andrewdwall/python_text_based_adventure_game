import room
from items import Magical_Sword
from npc import Enemy


# Create Player Class
class Player:

    def __init__(self, name):
        self.name = name
        self.current_room = "hall"
        self.inventory = []
        self.health = 100

    # Create method to move between rooms
    def move(self, direction):
        if direction in room.rooms[self.current_room]["exits"]:
            self.current_room = room.rooms[self.current_room]["exits"][direction]
            # Change room name output on move to correct grammar for readability
            if self.current_room == "wizards_quarters":
                print("You move to the Wizard's Quarters.")
            else:
                print(f"You move {direction} to the {self.current_room.capitalize()}.")
        else:
            print("You can't go that way.")
    
    # Create method to search room for items
    def search(self):
        current_room_items = room.rooms[self.current_room]["items"]
        if current_room_items:
            print(f"Available items in {self.current_room.capitalize()}: {[item.item_name for item in current_room_items]}")
        else:
            # Change room name output on search to correct grammar for readability
            if self.current_room == "wizards_quarters":
                print("There are no items to pick up in the Wizard's Quarters.")
            else:
                print(f"There are no items to pick up in the {self.current_room.capitalize()}")

    # Create method to pick up items
    def pickup(self, item_name):
        # Check if item's name in current room is the same as item's name specified in input
        current_room_items = room.rooms[self.current_room]["items"]
        for item in current_room_items:
            if item.item_name.lower() == item_name.lower():
                self.inventory.append(item)
                current_room_items.remove(item)
                print(f"You picked up the {item.item_name}.")
                return
        print("That item is not here.")

    # Create method to attack enemy
    def attack(self, enemy_name):
        # Set enemy in room to none initially, prevents referencing an undefined variable if player inputs invalid enemy name
        enemy = None
        # Check if enemy's name in current room is the same as enemy's name specified in input
        current_room_npc = room.rooms[self.current_room].get("npc")
        if current_room_npc and current_room_npc.name.lower() == enemy_name.lower():
            enemy = current_room_npc
        if isinstance(enemy, Enemy):
            # Check if player has the Magical Sword in their inventory
            if any(isinstance(item, Magical_Sword) for item in self.inventory):
                print(f"You swing your magical sword at {enemy.name}!")
                enemy.health -= 10
                print(f"{enemy.name} health: {enemy.health}")
                # Trigger enemy counterattack
                if enemy.health >0:
                    enemy.imp_attack(self)
                else:
                    if enemy.health <= 0:
                        print(f"You have defeated {enemy.name}!")
                        # Remove enemy from room on defeat
                        room.rooms[self.current_room]["npc"] = None
            else:
                print("You don't have a weapon to attack!")
        else:
            print("That enemy is not here.")