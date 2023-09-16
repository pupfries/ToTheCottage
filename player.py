# A module for the cottage character class
#import pygame


class Player:
    """Class for the player's character."""

    def __init__(self):
        """Initialize player and attributes."""
        self.achievements = []
        self.poss_endings = [
            "Rest Easy: You got the best ending! You remembered everything and got home in one piece.",
            "Westward: You died the absolute first chance you got! But don't beat yourself up! You can always try again :)",
            "So Close, Yet So Far: You made the last wrong choice in the game. One more lucky break and you'd have gotten the good ending. Oof!",
            "Pretty Good: Pat yourself on the back, you got home safe and sound! You didn't recover your memory but you got home safely!"
        ]
        self.inventory = []
        self.name = ""
        self.ending = ""
        self.poss_achievements = [
            "Hat Hair: You put on the moon hat!",
            "La Flor: You picked up the flower!",
            "The Truth, The Whole Truth: You remembered everything with the healing flower tea!",
            "Hunting Season: You met the nearby townsfolk!",
            "Stared In The Face of Death: You escaped the water monster!",
            "Lunatic: You were assimilated by the moon!",
            "Eren Jaeger: You were eaten by the monster!",
            "Home Sweet Home: You made it home!",
        ]

    def name_character(self):
        """Takes a name from the player for the character."""
        while True:
            name = input("What is your name?\n ").lower().strip()
            self.name = name.title()

            name_check = input(f"Your name is {self.name}. Is this right?\n ")
            if name_check.lower().strip() == "yes":
                break
            elif name_check.lower().strip() == "no":
                continue

        print(f"Welcome to the forest, {self.name}!")

    def see_inventory(self):
        """Reads contents of the inventory."""
        print("Your inventory contains: ")
        for item in self.inventory:
            print(item)

    def update_inventory(self, item):
        """Adds item to inventory."""
        self.inventory.append(item)

        print(f"{item.title()} has been added to inventory.")

    def remove_inventory_item(self, item):
        """Removes an item from the inventory."""
        removed_item = self.inventory.pop(item)

        print(f"{removed_item} has been removed from the inventory.")

    def reset_character(self):
        """Resets inventory, ending, achievements, and name."""
        self.inventory.clear()
        self.achievements.clear()
        self.ending = None

    def update_achievements(self, n):
        """Updates achievements of the character based on actions."""
        self.achievements.append(self.poss_achievements[n])

    def assign_ending(self, n):
        """Assigns one ending to the player."""
        self.ending = self.poss_endings[n]


# Tests
if __name__ == "__main__":
    stella = Player()
    stella.name_character()
    stella.update_inventory("cookie jar")
    stella.see_inventory()
