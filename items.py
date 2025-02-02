# Create Item class
class Item():

    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    
    # Create getter and setter methods for returning item name and description
    def get_item_name(self):
        return self.item_name

    def get_description(self):
        return self.item_description

    def set_item_name(self, item_name):
        self.item_name = item_name

    def set_description(self, item_description):
        self.item_description = item_description

    def describe_item(self):
        print(self.item_description)

# Create subclass for each unique item
class Glowing_Mushroom(Item):

    def __init__(self, item_name, item_description):
        super().__init__(item_name, item_description)


class Spellbook(Item):

    def __init__(self, item_name, item_description):
        super().__init__(item_name, item_description)


class Healing_Potion(Item):

    def __init__(self, item_name, item_description):
        super().__init__(item_name, item_description)


class Magical_Sword(Item):

    def __init__(self, item_name, item_description):
        super().__init__(item_name, item_description)