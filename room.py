# Create Rooms with descriptions and exits
rooms = {
    "hall": {
        "description": "You have entered the ground floor of a magical tower. There are doors to the east and north.",
        "exits": {"north": "library", "east": "apothecary"},
        "items": [] # Empty list to store items in room
    },
    "apothecary": {
        "description": "A dim room filled with alchemic reagents. An alchemist pours over a workstation. A door leads west to the hall.",
        "exits": {"west": "hall"},
        "items": []
    },
    "library": {
        "description": "Long rows of bookcases line the room, it seems to continue forever. A wizard is levitating through the aisles. A door leads south to the hall and a staircase leads up to the Wizard's Quarters.",
        "exits": {"south": "hall", "up": "wizards_quarters"},
        "items": []
    },
    "wizards_quarters": {
        "description": "A study filled with magical artifacts. An imp leaps round setting fire to the furnishings. A staircase leads down to the library.",
        "exits": {"down": "library"},
        "items": []
    }
}