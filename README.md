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
- move <direction> - Move to another room
- search - Search the room for items
- pickup <item> - Pick up an item in the room ***Requires fix***
- inventory - View items in inventory
- inspect - Inspect NPC in the current room to receive a description of them
- speak - Speak with the NPC in the current room
- trade - Trade with the NPC in the current room ***Requires test***
- attack <enemy> - Engage in combat with enemy in current room ***Requires addition and test***
- quit - Exit the game

## 🛠️ Features
- 🗺️ **Exploration** Navigate through different rooms with unique descriptions.
- 🧙‍♂️ **NPC Interactions** Engage with friendly and hostile NPCs.
- 🎒 **Inventory System** Collect and trade items. ***Requires fix***
- 🗡️ **Combat Mechanics** Battle enemies and gain rewards. ***To be implemented***

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

## 🔧 Development and Bug Fixes
- **Fix item pickup mechanism**
- **Test trade mechanics**
- **Add enemy combat to game Loop and test**

## 🛤️ Future Plans & Expansion
- 🏆 **Add Loot System** Add dropped items from enemies.
- 🔥 **Companion System** Implement summoning mechanic for imp with acquired item after defeat.
- 🏹 **Develop Combat and Health Mechanics** Create new enemies, attack types and healing action.
- 🎭 **Character Customisation** Include ability to choose player name and class mechanics.
- 🏔️ **Expand World** Add complexity to story and exploration of new locations.

## 📝 Changelog

### Version 1.0 (Jan 2025)
- Initial release with 3 explorable rooms and NPC speak interaction.