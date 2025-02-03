from player import Player
import room
from npc import Alchemist, Wizard, Imp
from items import Glowing_Mushroom, Spellbook, Magical_Sword, Healing_Potion


# Create instance of player character
player = Player("Hero")

# Create instances of NPCs
alchemist = Alchemist("Alchemist", "An alchemist brewing a curious mixture in a cauldron, he seems overwhelmed.", "Quick pass me that glowing mushroom over there! I need to complete this batch of potion", "glowing mushroom", "healing potion")
wizard = Wizard("Wizard", "A wizard dressed in long robes, he is searching the shelves for something.", "My spell backfired and I lost control of my summoned imp. It is locked in my quarters. I need to find my spellbook to banish it.", "spellbook", "magical sword")
imp = Imp("Imp", "A small fiend surrounded by an aura of fire.", "The imp speaks in a demonic tongue that you can't understand.")

# Assign NPCs to rooms
room.rooms["apothecary"]["npc"] = alchemist
room.rooms["library"]["npc"] = wizard
room.rooms["wizards_quarters"]["npc"] = imp

# Create instances room items
glowing_mushroom = Glowing_Mushroom("Glowing Mushroom", "A bioilluminescent fungus that has a green glow. It has alchemical properties.")
spellbook = Spellbook("Spellbook", "A tome of arcane sigils and incantations.")

# Assign items to rooms
room.rooms["apothecary"]["items"] = [glowing_mushroom]
room.rooms["library"]["items"] = [spellbook]

# Create game loop to include each method
def game_loop():

    last_room = None  # Track last room the player was in
    while True:
        # Print room description
        if player.current_room != last_room:
            print(f"\n{room.rooms[player.current_room]['description']}")
            last_room = player.current_room

        command = input("> ").lower().split()  # Displays > and awaits case-insensitive user input

        if len(command) == 0:
            continue

        if command[0] in ["move"]:
            if len(command) > 1:
                player.move(command[1])
            else:
                print("Move where?")

        elif command[0] == "search":
            player.search()

        elif command[0] in ["pickup"]:
            if len(command) > 1:
                item_name = " ".join(command[1:])
                item_name = item_name.lower()
                player.pickup(item_name)
            else:
                print("Specify item to pick up")
        
        elif command[0] == "inspect":
            npc = room.rooms[player.current_room].get("npc")
            if npc:
                npc.inspect()
            else:
                print("There is no one else here.")

        elif command[0] == "speak":
            npc = room.rooms[player.current_room].get("npc")
            if npc:
                npc.speak()
            else:
                print("There's no one to talk to here.")

        elif command[0] == "trade":
            npc = room.rooms[player.current_room].get("npc")
            if npc:
                npc.trade(player)
            else:
                print("You need the required item to trade.")
    
        elif command[0] == "inventory":
            print(f"Inventory: {', '.join(item.item_name for item in player.inventory) if player.inventory else 'Empty'}")

        elif command[0] == "quit":
            print("End adventure?")
            break
        else:
            print("Invalid command.")

# Run game
if __name__ == "__main__":
    game_loop()