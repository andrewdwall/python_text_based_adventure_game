# 🏰 Text-Based Adventure Game
An interactive text-based adventure game involving the player exploring different rooms of a tower, interacting with NPCs, collecting items, trading and engaging enemies in combat.

## 📜 About the Project
This project was designed to practice and showcase the implementation of Python concepts, including object-oriented programming, data structures and game logic.

## 🎮 How to Play
1. Run the game using Python:
```sh
python main.py
```

2. Use text commands to interact with the game:
- `move <direction>` - Move to another room
- `search` - Search the room for items
- `pickup <item name>` - Pick up an item in the room
- `inventory` - View items in inventory
- `inspect` - Inspect NPC in the current room to receive a description of them
- `speak` - Speak with the NPC in the current room
- `trade` - Trade with the NPC in the current room
- `attack <enemy name>` - Engage in combat with an enemy in the current room
- `quit` - Exit the game

## 🛠️ Features
- 🗺️ **Exploration** Navigate through different rooms with unique descriptions.
- 🧙‍♂️ **NPC Interactions** Engage with friendly and hostile NPCs.
- 🎒 **Inventory System** Collect and trade items.
- 🗡️ **Combat Mechanics** Battle enemies and gain rewards.

## 📂 File Structure
```
📂 Text-Adventure-Game  
 ┣ 📄 main.py            # Main game loop  
 ┣ 📄 player.py          # Player class definitions and mechanics  
 ┣ 📄 room.py            # Room definitions  
 ┣ 📄 items.py           # Item definitions and inventory system  
 ┣ 📄 npc.py             # NPC definitions and interactions  
 ┣ 📄 README.md          # Project documentation  
```

## 🚀 Installation & Requirements
- Python 3.x required

## 🛤️ Future Plans & Expansion
- 🏆 **Add Loot System** Add dropped items from enemies.
- 🔥 **Companion System** Implement summoning mechanic for imp with acquired item after defeat.
- 🏹 **Develop Combat and Health Mechanics** Create new enemies, attack types and healing action.
- 🎭 **Character Customisation** Include ability to choose player name and class mechanics.
- 🏔️ **Expand World** Add complexity to story, new NPCs and exploration of new locations.

## 🔧 Development and Bug Fixes
- **Expand NPC dialogue to update dynamically based on game progress**
- **Update inspect, speak and trade methods/commands to specify NPC name, allowing future addition of multiple NPCs in one room**

## 📝 Changelog

### Version 1.2.1 (Feb 2025)
- ✅ Updated formatting for room names, room descriptions and item names for better output readability.

### Version 1.2 (Feb 2025)
- ✅ Implemented combat by updating player attack method to check for sword in inventory, enemy in room and enemy specified in attack command. Added player attack to game loop.
- ✅ Added turn-based Imp attack to occur following player attack.
- ✅ Combat mechanics tested and working.
- ✅ Fixed error when attempting to trade with enemy.
- ✅ Fixed quit command to allow player to continue adventure.
- ✅ Output formatting improvements.

### Version 1.1.1 (Feb 2025)
- ✅ Fixed reward items to now be instantiated as objects in the npc.py trade method and removed instances of reward items from main.py. Inventory now functioning with reward objects.

### Version 1.1 (Feb 2025)
- ✅ Fixed item pickup mechanism.
- ✅ Trade mechanics tested and working.
- ✅ Changed room description to print only on movement between rooms and not after every action.


### Version 1.0 (Jan 2025)
- Initial release with 3 explorable rooms and NPC speak interaction.