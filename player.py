import room


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
            print(f"You move {direction} to the {self.current_room}.")
        else:
            print("You can't go that way.")
    
    # Create method to search room for items
    def search(self):
        current_room_items = room.rooms[self.current_room]["items"]
        if current_room_items:
            print(f"Available items in {self.current_room}: {[item.item_name for item in current_room_items]}")
        else:
            print(f"There are no obtainable items to in the {self.current_room}.")

    # Create method to pick up items
    def pickup(self, item_name):
        current_room_items = room.rooms[self.current_room]["items"]
        for item in current_room_items:
            if item.item_name.lower() == item_name.lower():
                self.inventory.append(item)
                current_room_items.remove(item)
                print(f"You picked up the {item.item_name}.")
                return
        print("That item is not here.")

    # Create method to attack enemy
    def attack(self, enemy):
        if enemy in room.rooms[self.current_room]["enemy"]:
            room.rooms[self.current_room]["enemy"].health -= 10
            print(f"You swing your magical sword at the {enemy.name}.\n {enemy.name} health: {enemy.health}")