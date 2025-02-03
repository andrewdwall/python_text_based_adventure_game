from player import Player
import room
from npc import Alchemist, Wizard, Imp
from items import Glowing_Mushroom, Spellbook


# Create instance of player character
player = Player("Hero")

# Create instances of NPCs
alchemist = Alchemist("Alchemist", "An alchemist brewing a curious mixture in a cauldron, he seems overwhelmed.", "Quick! pass me that Glowing Mushroom over there! I need to complete this batch of potion", "glowing mushroom", "healing potion")
wizard = Wizard("Wizard", "A wizard dressed in long robes, he is searching the shelves for something.", "My spell backfired and I lost control of my summoned Imp. It is locked in my quarters. I need to find my Spellbook to banish it.", "spellbook", "magical sword")
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
                print("Specify direction to move.")

        elif command[0] == "search":
            player.search()

        elif command[0] in ["pickup"]:
            if len(command) > 1:
                # Check if item to pick up is item name specified
                item_name = " ".join(command[1:])
                item_name = item_name.lower()
                player.pickup(item_name)
            else:
                print("Specify item to pick up.")
        
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
                # Check if NPC is able to trade
                if hasattr(npc, 'trade'):
                    npc.trade(player)
                else:
                    print(f"You can't trade with {npc.name}.")
            else:
                print("There is no one to trade with.")
    
        elif command[0] == "inventory":
            print(f"Inventory: {', '.join(item.item_name for item in player.inventory) if player.inventory else 'Empty'}")

        elif command[0] == "attack":
            if len(command) > 1:
                # Check if enemy to attack is enemy name specified
                enemy_name = " ".join(command[1:])
                player.attack(enemy_name)
            else:
                print("Specify an enemy to attack.")

        elif command[0] == "quit":
            confirm = input("End adventure? (yes/no): ")
            if confirm == "yes":
                print("Farewell.")
                break
            else:
                print("Continue adventure.")
        else:
            print("Invalid command.")

# Run game
if __name__ == "__main__":
    game_loop()