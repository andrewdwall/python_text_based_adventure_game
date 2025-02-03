from items import Glowing_Mushroom, Spellbook, Magical_Sword, Healing_Potion


# Create NPC class
class NPC():

    def __init__(self, name, description, dialogue):
        self.name = name
        self.description = description
        self.dialogue = dialogue
    
    # Create inspect and speak methods for NPCs
    def inspect(self):
        print(f"{self.description}")

    def speak(self):
        print(f"{self.name}: '{self.dialogue}'")


# Create Friend subclass
class Friend(NPC):

    def __init__(self, name, description, dialogue, required_item, reward):
        super().__init__(name, description, dialogue)
        self.required_item = required_item
        self.reward = reward
        self.friend = True


# Create Alchemist subclass
class Alchemist(Friend):

    def __init__(self, name, description, dialogue, required_item, reward):
        super().__init__(name, description, dialogue, required_item, reward)
    
    # Create trade method for Alchemist
    def trade(self, player):
        for item in player.inventory:
            if isinstance(item, Glowing_Mushroom):
                print(f"{self.name}: Thank you for the reagent. My mixture is now ready. Take this for your travels.\n{self.name} gives you {self.reward.capitalize()}!")
                player.inventory.remove(item)
                player.inventory.append(Healing_Potion("Healing Potion", "A ruby-coloured liquid in a vial. Restores 10 health points."))
                return
        print(f"{self.name}: '{self.dialogue}'\n(You need a Glowing Mushroom.)")


# Create Wizard subclass
class Wizard(Friend):

    def __init__(self, name, description, dialogue, required_item, reward):
        super().__init__(name, description, dialogue, required_item, reward)

    # Create trade method for Wizard
    def trade(self, player):
        for item in player.inventory:
            if isinstance(item, Spellbook):
                print(f"{self.name}: You have found my Spellbook! If I create you a sword would you take care of that imp for me?\n{self.name} gives you {self.reward.capitalize()}!")
                player.inventory.remove(item)
                player.inventory.append(Magical_Sword("Magical Sword", "A sword imbued with magical energy. It is effective in banishing summoned creatures."))
                return
        print(f"{self.name}: '{self.dialogue}'\n(You need a Spellbook.)")


# Create Enemy subclass
class Enemy(NPC):

    def __init__(self, name, description, dialogue):
        super().__init__(name, description, dialogue)
        self.enemy = True


# Create Imp subclass
class Imp(Enemy):

    def __init__(self, name, description, dialogue):
        super().__init__(name, description, dialogue)
        self.health = 40

    # Create method for Imp attack
    def imp_attack(self, player):
        print(f"{self.name} hurls a fireball at you!")
        player.health -= 10
        print(f"{player.name} health: {player.health}")
        if player.health <= 0:
            print("You have been defeated.")
            exit()