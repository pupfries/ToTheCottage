# Main script for the game To The Cottage
import time
from player import Player


class ToTheCottage:
    """A class to manage the game, resources, and attributes."""

    def __init__(self):
        """Initialize attributes."""

        # Formatting
        self.spacer = "\n~~~~~~~~~~\n"

        # Imports
        self.character = Player()

        # Choices for each question
        self.choices = []

        # Start game
        self.start = self._start_game()

    # This section contains each major choice as its own function
    def first_question(self):
        """Gives player their first major choice"""
        # Major choice 1, intro question
        self._read_file("intro.txt")
        self._give_choices("look around", "try to remember", "get up")
        answer = None
        #   allow player to use every choice before moving on
        while answer != self.choices[2]:
            answer = self._get_answer("What do you want to do?")
            if answer == self.choices[0]:
                self._read_file("c1a.txt")
            elif answer == self.choices[1]:
                self._read_file("c1b.txt")
        if answer == "get up":
            self._read_file("cp1.txt")

    def second_question(self):
        """Gives player their second major choice, which way to travel."""
        # Major choice 2, ask player which way to travel
        self._give_choices("north", "south", "east", "west")
        answer = self._get_answer(
            "Which direction do you want to travel in?")
        #   player chooses north
        if answer == self.choices[0]:
            self._read_file("north.txt")
            self._give_choices("left", "right")
            self._get_answer("Which way?")
            if answer == self.choices[0]:
                self._read_file("northl.txt")
                self.character.update_achievements(3)
                self.inactive("dead")
            elif answer == self.choices[1]:
                self._read_file("northr.txt")
                self._give_choices("yes", "no")
                self._get_answer("Take flower?")
                if answer == self.choices[0]:
                    self._read_file("northr1.txt")
                    self.character.update_inventory("flower")
                elif answer == self.choices[1]:
                    self._read_file("northr2.txt")
        #   player chooses south
        elif answer == self.choices[1]:
            self._read_file("south.txt")
            self._give_choices("yes", "no")
            self._get_answer("Pick up the hat?")
            if answer == self.choices[0]:
                self._read_file("south1.txt")
                self.character.update_inventory("hat")
            elif answer == self.choices[1]:
                self._read_file("south2.txt")

            self._read_file("southcp1.txt")
            self._give_choices("go to stream", "continue")
            self._get_answer("Go to the stream or continue ahead?")
            if answer == self.choices[0]:
                self._read_file("stream1.txt")
            elif answer == self.choices[1]:
                self._read_file("stream2.txt")
                self.inactive("dead")
        #   player chooses east
        elif answer == self.choices[2]:
            self._read_file("east.txt")
            self._give_choices("yes", "no")
            self._get_answer("Take the flower?")
            if answer == self.choices[0]:
                self._read_file("east1.txt")
                self.character.update_inventory("flower")
            elif answer == self.choices[1]:
                self._read_file("east2.txt")
        #   player chooses west, game over
        elif answer == self.choices[3]:
            self._read_file("west.txt")
            self.character.assign_ending(1)
            self.inactive("dead")

    def third_question(self):
        """Asks player 3rd major choice, look at the moon or not."""
        # Major choice 3, whether to look at the moon
        self._read_file("cp2a.txt")
        #   if player has hat
        if "hat" in self.character.inventory:
            self._read_file("cp2b.txt")
        #   if player doesn't have hat
        elif "hat" not in self.character.inventory:
            self._give_choices("hide", "look")
            self._get_answer("Do you hide or continue and look?")
            #   player hides
            if answer == self.choices[0]:
                self._read_file("hide.txt")
                self._give_choices("leaf", "bush")
                self._get_answer(
                    "Do you take a leaf or hide behind the bush?")
                if answer == self.choices[0]:
                    self._read_file("hide1.txt")
                elif answer == self.choices[1]:
                    self._read_file("hide2.txt")
            #   player looks at the moon, game over
            elif answer == self.choices[1]:
                self._read_file("look.txt")
                self.inactive("dead")

    def fourth_question(self):
        """Gives player 4th major choice, whether to enter the boat."""
        # Major choice 4, whether to get in the boat
        self._read_file("cp3.txt")
        self._give_choices("yes", "no")
        self._get_answer("Get in the boat?")
        #   player gets in the boat
        if answer == self.choices[0]:
            self._read_file("boat1.txt")
            self._give_choices("paddle", "look")
            self._get_answer("Do you paddle harder or look and see?")
            if answer == self.choices[0]:
                self._read_file("boat1a.txt")
            elif answer == self.choices[1]:
                self._read_file("boat1b.txt")
                self.character.update_achievements(5)
                self.inactive("dead")

            self._read_file("boatcp1.txt")
            self._give_choices("stay", "get out")
            self._get_answer("Do you stay in the boat or get out?")
            if answer == self.choices[0]:
                self._read_file("boat3a.txt")
            elif answer == self.choices[1]:
                self._read_file("boat3b.txt")
                self._give_choices("flee", "fight")
                self._get_answer("Do you flee or fight?")
                if answer == self.choices[0]:
                    self._read_file("boat3b1.txt")
                    self.character.update_achievements(4)
                elif answer == self.choices[1]:
                    self._read_file("boat3b2.txt")
                    self.character.update_achievements(6)
                    self.inactive("dead")

            self._read_file("cp4.txt")
        #   player doesn't get in boat, game over
        elif answer == self.choices[1]:
            self._read_file("boat2.txt")
            self.inactive("dead")

        # Special passage if player has flower, amnesia recovery
        if "flower" in self.character.inventory:
            self._read_file("cp5a.txt")
            self.character.update_achievements(2)
        elif "flower" not in self.character.inventory:
            self._read_file("cp5b.txt")

    def fifth_question(self):
        """Gives player 5th major choice, path or bridge."""
        # Special passage if player has flower, amnesia recovery
        if "flower" in self.character.inventory:
            self._read_file("cp5a.txt")
            self.character.update_achievements(2)
        elif "flower" not in self.character.inventory:
            self._read_file("cp5b.txt")

        # Major choice 5, path or bridge
        self._give_choices("bridge", "path")
        self._get_answer(
            "Cross the bridge or follow the path into the forest?")
        #   player crosses bridge
        if answer == self.choices[0]:
            self._read_file("bridge.txt")
            self._give_choices("approach", "walk")
            self._get_answer("Will you approach the tree or walk past it?")
            if answer == self.choices[0]:
                self._read_file("tree1.txt")
            elif answer == self.choices[1]:
                self._read_file("tree2.txt")

            self._read_file("bridgecp1.txt")
            self._give_choices("star", "cave", "puddle", "tree")
            self._get_answer("How do you proceed?")
            if answer == self.choices[0]:
                self._read_file("bridges.txt")
                self.character.assign_ending(2)
                self.inactive("dead")
            elif answer == self.choices[1]:
                self._read_file("bridgec.txt")
                self.character.assign_ending(2)
                self.inactive("dead")
            elif answer == self.choices[2]:
                self._read_file("bridgep.txt")
            elif answer == self.choices[3]:
                self._read_file("bridget.txt")
                self.character.assign_ending(2)
                self.inactive("dead")
        #   player takes path, game over
        elif answer == self.choices[1]:
            self._read_file("path.txt")
            self.character.assign_ending(2)
            self.inactive("dead")

    def sixth_question(self):
        """Gives player last major choice."""
        # Major choice 6, last choice, enter cottage
        self._read_file("cp6.txt")
        self._give_choices("survey", "enter", "observe")
        answer = None

        while answer != self.choices[1]:
            answer = self._get_answer(
                "Survey the yard, walk inside, or observe the cottage?")
            if answer == self.choices[0]:
                self._read_file("survey_yard.txt")
            elif answer == self.choices[2]:
                self._read_file("observe_house.txt")
        if answer == self.choices[1]:
            self._read_file("walk_in.txt")

        self._read_file("cp7.txt")

        #   special passage if hat
        if "hat" in self.character.inventory:
            self._read_file("cp8a.txt")
        elif "hat" not in self.character.inventory:
            self._read_file("cp8b.txt")

        self._read_file("cp9.txt")

    def run_game(self):
        """A method which handles the main loop of the game."""

        while self.start:
            self.first_question()
            self.second_question()
            self.third_question()
            self.fourth_question()
            self.fifth_question()
            self.sixth_question()

            # Good ending
            self.character.assign_ending(0)
            self.inactive("alive")

    def _start_game(self):
        """Allow user to begin game."""
        print(self.spacer)
        print(f"Welcome to: To the Cottage")
        print("\nThis is a text-based choose-your-own-adventure game.")
        time.sleep(1)
        print("\nYou have quite the journey ahead of you.")
        time.sleep(0.8)
        start = input("\nStart the journey?\n\t>>> ").lower().strip()
        if start == "yes":
            start = True
        elif start == "no":
            start = False

        return start

    def _get_answer(self, question):
        """Prompt user for input."""
        answer = None
        while answer not in self.choices:
            # Gives question and lists answers
            print(f"\n{question}\n")
            time.sleep(0.5)
            print(f"\nType one of the following:")
            for self.choice in self.choices:
                print(self.choice)
            
    def _give_choices(self, *args):
        """Creates choices for the user to select from."""
        self.choices.clear()
        for arg in args:
            self.choices.append(arg)

    def _read_file(self, filepath):
        """Display story text to player."""
        full_filepath = "C:/Users/tymia/OneDrive/Desktop/python_work/"
        full_filepath += "personal_projects/To The Cottage/text/" + filepath
        with open(full_filepath) as file_obj:
            contents = file_obj.read()
        time.sleep(0.8)
        print(f"\n{contents}\n")
        time.sleep(4)
        print(f"{self.spacer}")

    def inactive(self, status):
        """Starts the end screen, displays stats if any."""

        if status == "reject":
            print("\nOkay, bye!")
        elif status in ["dead", "alive"]:
            time.sleep(0.05)
            print(
                "\n########################################"
                "\n#                                      #"
                "\n#        GAME STATS END SCREEN         #"
                "\n#                                      #"
                "\n########################################"
            )
            if status == "dead":
                print("\nDamn, you died fr.")
            elif status == "alive":
                print("\nYou made it! Look at you!!!")
                self.character.update_achievements(7)

            if "hat" in self.character.inventory:
                self.character.update_achievements(0)
            if "flower" in self.character.inventory:
                self.character.update_achievements(0)
            elif "flower" not in self.character.inventory:
                self.character.assign_ending(3)

            if self.character.achievements:
                time.sleep(0.4)
                print("\nCongrats! You got acheivements: ")
                for achievement in self.character.achievements:
                    time.sleep(0.4)
                    print("\n{achievement}")
            if self.character.ending:
                print("Ooh! You got a cool ending:")
                time.sleep(0.3)
                print(f"\n\t{self.character.ending}")

        # Prompt for replay
        replay_options = ["yes", "no"]
        replay = None
        while replay not in replay_options:
            time.sleep(0.5)
            replay = input("\n\nPlay again?\n ").lower().strip()

        if replay == "yes":
            self.character.reset_character()
            self._start_game()
        elif replay == "no":
            pass


if __name__ == "__main__":
    ttc = ToTheCottage()
    ttc.run_game()
