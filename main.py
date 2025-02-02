from player import Player
import room
from npc import Alchemist, Wizard, Imp
from items import Glowing_Mushroom, Spellbook, Magical_Sword, Healing_Potion


# Create instance of player character
player = Player("Hero")

# Create instances of NPCs
alchemist = Alchemist("Alchemist", "An alchemist brewing a curious mixture in a cauldron, he seems overwhelmed.", "Quick pass me that glowing mushroom over there! I need to complete this batch of potion", "glowing mushroom", "healing potion")
wizard = Wizard("Wizard", "A man dressed in long robes, he is searching the shelves for something.", "My spell backfired and I lost control of my summoned imp. It is locked in my quarters. I need to find my spellbook to banish it.", "spellbook", "magical sword")
imp = Imp("Imp", "A small fiend surrounded by an aura of fire.", "The imp speaks in a demonic tongue that you can't understand.")

# Assign NPCs to rooms
room.rooms["apothecary"]["npc"] = alchemist
room.rooms["library"]["npc"] = wizard
room.rooms["wizards_quarters"]["npc"] = imp

# Create instances of items
glowing_mushroom = Glowing_Mushroom("Glowing Mushroom", "A bioilluminescent fungus that has a green glow. It has alchemical properties.")
spellbook = Spellbook("Spellbook", "A tome of arcane sigils and incantations.")
magical_sword = Magical_Sword("Magical Sword", "A sword imbued with magical energy. It is effective in banishing summoned creatures.")
healing_potion = Healing_Potion("Healing Potion", "A ruby coloured liquid in a vial. Restores 10 health points.")

# Assign items to rooms
room.rooms["apothecary"]["items"] = [glowing_mushroom]
room.rooms["library"]["items"] = [spellbook]

# Create game loop to include each method
def game_loop():
    while True:
        print(f"\n{room.rooms[player.current_room]['description']}")  # Print room description

        command = input("> ").lower().split()

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
                player.pickup(command[1])
            else:
                print("No item to pick up.")
        
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
            print(f"Inventory: {', '.join(item.item_name for item in player.inventory)}")

        elif command[0] == "quit":
            print("End adventure?")
            break
        else:
            print("Invalid command.")

# Run game
if __name__ == "__main__":
    game_loop()