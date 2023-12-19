from backpack import Item
class Character(Item):
    def __init__(self, character_name, location, desired_item, held_item):
        # Initialize the base class with the attributes of held_item if it's not None
        super().__init__(held_item.item_name, held_item.desc) if held_item else None

        self.character_name = character_name
        self.location = location

        # Check if desired_item is not None before creating a new Item instance
        if desired_item is not None:
            self.desired_item = Item(desired_item.item_name, desired_item.desc)
        else:
            self.desired_item = None

        #print(f"Debug: {character_name}'s desired_item: {self.desired_item}")

        # Ensure held_item is an instance of Item, or create an empty Item if None
        self.held_item = Item("", "") if held_item is None else held_item

    def greet_player(self):
        print(f"{self.character_name}: Welcome to {self.location}!")


    # def offer_item(self):
    #     if self.held_item:
    #         print(f"{self.character_name}: I think you have something I want! Let's swap. {self.held_item.item_name} may be useful for you in the future.")
    #     else:
    #         print(f"{self.character_name}: I think you have something I want! Let's swap.")

    def change_item_held(self, item):
        self.held_item = item