# Importing everything that is necessary for the game such as external libraries and seperate files
from room import Room
from text_ui import TextUI
from characters import Character
from hangman import HangmanGame
from backpack import Backpack
from backpack import NotInBackpackError
from backpack import Item
import time
import random
import logging

logging.basicConfig(filename='game_log.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Main game class
class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        # Set up logging and everything else that needs initialising
        logging.info("Game started")
        self.create_rooms()
        self.current_room = self.Pyramids
        self.textUI = TextUI()
        self.player_name = None
        self.backpack = Backpack(2)
        self.hangman_words = ["limestone", "mummy", "gold"]
        self.game_over = False

        self.item1=Item('Ancient Amulet', 'An ancient amulet with mysterious engravings.')
        self.item2=Item('Incan Relic', 'A relic from the Incan civilisation adorned with intricate patterns.')
        self.item3=Item('Spirit Stone', 'A mystical stone said to have spiritual powers.')
        self.item4=Item('Timeless Tapestry', 'A tapestry that seems to transcend time, showcasing various historical events.')
        self.item5=Item('Druidic Culture', 'A crystal with ties to ancient druidic rituals.')
        self.item6=Item('Polynesian Totem', 'A totem representing the rich culture of Polynesia')
        self.item7=Item('Mayan Glyph', 'A glyph from the Mayan civilisation, telling a story of their history.')
        self.item8=Item('Byzantine Icon', 'An intricately crafted icon from the byzantine era.')
        self.item9=Item('Gladiator Token', 'A token given to gladiators as a symbol of honour and bravery.')
        self.item10=Item('Nomads Compass', 'A special compass that guides bedouins through the desert sands.')

        self.char1 = Character('Sara the Archaeologist', 'Pyramids of Giza', None, self.item10)
        self.char2 = Character('Kai the Inca Guardian', 'Machu Picchu', self.item2, self.item3)
        self.char3 = Character(str('Rafiq the Desert Nomad'), str('Petra'), self.item10, self.item4)
        self.char4 = Character('Joao the Spirit Guide', 'Christ The Redeemer', self.item3, self.item6)
        self.char5 = Character('Raj the Timeless Artisan', 'Taj Mahal', self.item4, self.item2)
        self.char6 = Character('George the Druidic Keeper', 'Stonehenge', self.item5, self.item9)
        self.char7 = Character('Moana the Polynesian Explorer', 'Easter Island', self.item6, self.item7)
        self.char8 = Character('Javier the Mayan Historian', 'Chichen Itza', self.item7, self.item5)
        self.char9 = Character('Lucius the Gladiator Mentor', 'Colosseum', self.item9, self.item8)
        self.char10 = Character('Sofia the Byzantine Soldier', 'Hagia Sophia', self.item8, None)


    def create_rooms(self):
        """
            Sets up all room assets.
        :return: None
        """
        # Changed
        self.Petra = Room("You are in Petra, Jordan", 'Petra')
        self.Pyramids = Room("You are at the Pyramids of Giza in Egypt", 'Pyramids')
        self.Machu = Room("You are in Macchu Picchu in Peru", 'Machu')
        self.Redeemer = Room("You are the the Christ the Redeemer Statue in Brazil", 'Redeemer')
        self.Taj = Room("You are at the Taj Mahal in India", 'Taj')
        self.Stone = Room("You are at Stonehenge in England", 'Stone')
        self.Easter = Room("You are on Easter Island in Chile", 'Easter')
        self.Chichen = Room("You are at Chichen Itza in Mexico", 'Chichen')
        self.Hagia = Room ("You are at the Hagia Sophia in Turkiye", 'Hagia')
        self.Colosseum = Room("You are at the Colosseum in Italy", 'Colosseum')

        # Changed
        self.Pyramids.set_exit("1", self.Petra)
        self.Pyramids.set_exit("2", self.Machu)
        self.Petra.set_exit("1", self.Pyramids)
        self.Petra.set_exit("2", self.Taj)
        self.Petra.set_exit("3", self.Redeemer)
        self.Machu.set_exit("1", self.Pyramids)
        self.Machu.set_exit("2", self.Redeemer)
        self.Machu.set_exit("3", self.Taj)
        self.Redeemer.set_exit("1", self.Petra)
        self.Redeemer.set_exit("2", self.Machu)
        self.Redeemer.set_exit("3", self.Easter)
        self.Redeemer.set_exit("4", self.Stone)
        self.Taj.set_exit("1", self.Machu)
        self.Taj.set_exit("2", self.Petra)
        self.Taj.set_exit("3", self.Stone)
        self.Taj.set_exit("4", self.Easter)
        self.Stone.set_exit("1", self.Redeemer)
        self.Stone.set_exit("2", self.Taj)
        self.Stone.set_exit("3", self.Colosseum)
        self.Stone.set_exit("4", self.Chichen)
        self.Easter.set_exit("1", self.Taj)
        self.Easter.set_exit("2", self.Redeemer)
        self.Easter.set_exit("3", self.Chichen)
        self.Easter.set_exit("4", self.Colosseum)
        self.Chichen.set_exit("1", self.Stone)
        self.Chichen.set_exit("2", self.Easter)
        self.Chichen.set_exit("3", self.Hagia)
        self.Colosseum.set_exit("1", self.Easter)
        self.Colosseum.set_exit("2", self.Stone)
        self.Colosseum.set_exit("3", self.Hagia)
        self.Hagia.set_exit("1", self.Chichen)
        self.Hagia.set_exit("2", self.Colosseum)

    def check_room(self):
        if self.current_room.name == "Petra":
            self.do_petra_actions()
        elif self.current_room.name == "Machu":
            self.do_machu_actions()
        elif self.current_room.name == "Redeemer":
            self.do_redeemer_actions()
        elif self.current_room.name == "Taj":
            self.do_taj_actions()
        elif self.current_room.name == "Stone":
            self.do_stone_actions()
        elif self.current_room.name == "Easter":
            self.do_easter_actions()
        elif self.current_room.name == "Chichen":
            self.do_chichen_actions()
        elif self.current_room.name == "Hagia":
            self.do_hagia_actions()
        elif self.current_room.name == "Colosseum":
            self.do_colosseum_actions()

    def display_portal_options(self):
        # Check if the game has been won before printing the portal options
        if self.check_win_condition():
            return

        # Code for displaying portal options at each location
        if self.current_room.name == 'Machu':
            self.textUI.print_to_textUI("""
            Would you like to take:
            Portal 1 (Pyramids, Egypt),
            Portal 2 (Redeemer Statue, Brazil),
            or
            Portal 3 (Taj Mahal, India)
            """)
        elif self.current_room.name == "Petra":
            self.textUI.print_to_textUI("""
                Would you like to take:
                Portal 1 (Pyramids, Egypt),
                Portal 2 (Taj Mahal, India),
                or
                Portal 3 (Redeemer Statue, Brazil)
                """)
        elif self.current_room.name == 'Redeemer':
            self.textUI.print_to_textUI("""
            Would you like to take:
            Portal 1 (Petra, Jordan),
            Portal 2 (Machu Picchu, Peru),
            Portal 3 (Easter Island, Chile),
            or
            Portal 4 (Stonehenge, England)
            """)
        elif self.current_room.name == "Taj":
            self.textUI.print_to_textUI("""
                Would you like to take:
                Portal 1 (Machu Picchu, Peru),
                Portal 2 (Petra, Jordan),
                Portal 3 (Stonehenge, England),
                or Portal 4 (Easter Island, Chile)
                """)
        elif self.current_room.name == "Stone":
            self.textUI.print_to_textUI("""
            Would you like to take:
            Portal 1 (Redeemer Statue, Brazil),
            Portal 2 (Taj Mahal, India),
            Portal 3 (Colosseum, Italy),
            or
            Portal 4 (Chichen Itza, Mexico)
            """)
        elif self.current_room.name == 'Easter':
            self.textUI.print_to_textUI("""
            Would you like to take:
            Portal 1 (Taj Mahal, India),
            Portal 2 (Redeemer Statue, Brazil),
            Portal 3 (Chichen Itza, Mexico),
            or
            Portal 4 (Colosseum, Italy)
            """)
        elif self.current_room.name == 'Chichen':
            self.textUI.print_to_textUI("""
            Would you like to take:
            Portal 1, (Stonehenge, England)
            Portal 2, (Easter Island, Chile)
            or
            Portal 3 (Hagia Sophia, Turkiye),
            """)
        elif self.current_room.name == 'Colosseum':
            self.textUI.print_to_textUI("""
            Would you like to take:
            Portal 1 (Easter Island, Chile),
            Portal 2 (Stonehenge, England),
            or
            Portal 3 (Hagia Sophia, Turkiye)
            """)
        elif self.current_room.name == 'Hagia':
            self.textUI.print_to_textUI("""
            Would you like to take:
            Portal 1, (Chichen Itza, Mexico),
            or
            portal 2, (Colosseum, Italy)
            """)







    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        print(self.current_room.get_long_description())
        self.do_pyramids_actions()
        finished = False
        while not finished:
            self.check_room()
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)

            if self.game_over:
                finished = True

        print("Game Over!") # Changed
        return finished



        #self.current_room = self.Pyramids

        #self.do_pyramids_actions()

    def interact_with_character_swap(self, character_name):
        character = getattr(self, character_name, None)

        while character:
            desired_item = character.desired_item

            # Convert item names to lowercase strings for comparison
            backpack_contents = [item.item_name.lower() for item in self.backpack.contents]
            self.textUI.print_to_textUI(f"Backpack contents: {', '.join(backpack_contents)}\n")

            user_offered_item = self.textUI.get_user_input(
                f"What item do you offer to {character.character_name}? ").lower()

            if user_offered_item in [item.item_name.lower() for item in
                                     self.backpack.contents] and user_offered_item == desired_item.item_name.lower():
                final_text4 = (f"""You offered {user_offered_item} to {character.character_name}.
{character.character_name} accepted the offer.\n""")
                for char in final_text4:
                    print(char, end='', flush=True)
                    time.sleep(0.03)

                try:
                    offered_item = next(
                        (item for item in self.backpack.contents if item.item_name.lower() == user_offered_item), None)
                    if offered_item is not None:
                        self.backpack.remove_item(offered_item)
                        self.backpack.add_item(character.held_item)
                        final_text5 = (f"""{character.held_item.item_name} added to your backpack.
{character.held_item.desc}
Backpack contents: {', '.join(item.item_name for item in self.backpack.contents)}\n""")
                        for char in final_text5:
                            print(char, end='', flush=True)
                            time.sleep(0.03)
                        character.change_item_held(offered_item)

                    else:
                        self.textUI.print_to_textUI((f"Could not find {user_offered_item} in your backpack."))
                except NotInBackpackError:
                    self.textUI.print_to_textUI("An error occurred while removing the item from your backpack.")

                # Moved the win condition check and response outside of the try-except block
                if self.check_win_condition():
                    self.final_message()
                    self.game_over = True  # Set the game_over flag to True
                    return True

                # Exit the loop after successful interaction
                break
            else:
                self.textUI.print_to_textUI(
                    f"{character.character_name}: I don't need that. Give me the {desired_item.item_name.lower()}.\n")
                portal_choice = self.textUI.get_user_input("Do you want to use a portal? (yes/no): ").lower()
                if portal_choice == "yes":
                    break  # Exit the loop after using the portal
                elif portal_choice == "no":
                    continue  # Continue the loop and prompt for a new item
                else:
                    self.textUI.print_to_textUI("Invalid choice. Please enter 'yes' or 'no'.\n")

        # Outside the loop, check if the character is valid
        if not character:
            self.textUI.print_to_textUI("Invalid character. Please choose a valid character.\n")

        return False

    def game_loop(self):
        """ The main game loop"""
        finished = False
        while not finished:
            print("Current Room:", self.current_room)
            room_actions = self.get_room_actions()
            room_actions()
            if self.check_game_over():
                break


    def do_pyramids_actions(self):
        self.current_room = self.Pyramids
        final_text2 = ("""
            6:13pm Saturday, 8 April 2045
            Sara The Archaeologist:
            Welcome to the pyramids.
            I heard you're looking for the girl...
            You wouldn't be the first.
            Anyway, this task is not gonna be easy,
            if you complete this minigame,
            I'll give you something that may come in handy later \n""")
        for char in final_text2:
            print(char, end='', flush=True)
            time.sleep(0.03)

        while True:  # Add a loop to allow restarting the game
            hangman_word = random.choice(self.hangman_words)
            hangman_game = HangmanGame(hangman_word)

            self.textUI.print_to_textUI("Welcome to Hangman!")
            self.textUI.print_to_textUI("Try to guess the word")
            self.textUI.print_to_textUI(hangman_game.display_word())

            while '_' in hangman_game.display_word() and len(hangman_game.incorrect) < 5:
                user_guess = self.textUI.get_user_input("Enter a letter: ")
                if len(user_guess) == 1 and user_guess.isalpha():
                    result = hangman_game.make_guess(user_guess)
                    if result == True:
                        self.textUI.print_to_textUI("Correct!")
                    elif result == False:
                        self.textUI.print_to_textUI("Incorrect!")
                else:
                    self.textUI.print_to_textUI("Invalid input. Please enter a single letter.")

                self.textUI.print_to_textUI(hangman_game.display_word())

            if '_' not in hangman_game.display_word():
                self.textUI.print_to_textUI(" ")
                self.textUI.print_to_textUI("Congratulations! you guessed the word.")
                try:
                    self.backpack.add_item(self.item10)
                    self.textUI.print_to_textUI(f"{self.item10.item_name} added to your backpack.")
                    self.textUI.print_to_textUI(f"{self.item10.desc}")
                except NotInBackpackError:
                    self.textUI.print_to_textUI("There's not enough space in your backpack.")

            # Just here for now to check if it was actually added.
            item_to_check = self.item10.item_name
            if any(item.item_name == item_to_check for item in self.backpack.contents):
                print(f"{item_to_check} is in your backpack")

            if self.item10 in self.backpack.contents:
                final_text3 = (f"""
Two portals have opened up in front of you.
Would you like to take:
Portal 1 (Petra, Jordan)?
or
Portal 2? (Machu Picchu, Peru)
""")
                for char in final_text3:
                    print(char, end='', flush=True)
                    time.sleep(0.01)

                break  # Exit the loop if the player wins

            else:
                self.textUI.print_to_textUI("Sorry, you ran out of guesses.")
                self.textUI.print_to_textUI("Sara The Archaeologist: Better luck next time!\n")
                time.sleep(2)
                # Continue to the next iteration of the loop for a new game
    # continue later
    def do_machu_actions(self):
        self.char2.greet_player()
        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char2.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char2')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            machu_speech = f"{self.char2.character_name}: She spends most of her time on the beach."

            for char in machu_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)
            self.display_portal_options()
            self.check_win_condition()
            break

    def do_petra_actions(self):
        self.current_room = self.Petra
        self.char3.greet_player()

        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char3.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char3')
                # After interacting, display portal options and break the loop
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue

            petra_speech = f"{self.char3.character_name}: I heard that the girl you're looking for likes spicy food"

            for char in petra_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)

            self.display_portal_options()
            self.check_win_condition()
            break

    def do_redeemer_actions(self):
        self.char4.greet_player()

        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char4.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char4')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            redeemer_speech = f"{self.char4.character_name}: One time she said to me: 'Dum Dum Give Me Gum Gum'. I was speechless."

            for char in redeemer_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)
            self.display_portal_options()
            self.check_win_condition()
            break

    def do_taj_actions(self):
        self.char5.greet_player()
        while True:  # Keep asking until a valid response is given
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char5.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char5')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            taj_speech = f"{self.char5.character_name}: I saw her at the start of the Amazon River"

            for char in taj_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)
            self.display_portal_options()
            self.check_win_condition()
            break

    def do_stone_actions(self):
        self.char6.greet_player()

        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char6.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char6')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            stone_speech = f"{self.char6.character_name}: Her favourite food is pizza"

            for char in stone_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)
            self.display_portal_options()
            self.check_win_condition()
            break

    def do_easter_actions(self):
        self.char7.greet_player()

        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char7.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char7')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            easter_speech = f"{self.char7.character_name}: The last time i saw her was on the 5th of May"

            for char in easter_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)
            self.display_portal_options()
            self.check_win_condition()
            break

    def do_chichen_actions(self):
        self.char8.greet_player()

        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char8.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char8')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            chichen_speech = f"{self.char8.character_name}: When i saw her, i woke up in a red phone box"

            for char in chichen_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)
            self.display_portal_options()
            self.check_win_condition()
            break

    def do_hagia_actions(self):
        self.char10.greet_player()
        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char10.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char10')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            self.display_portal_options()
            self.check_win_condition()
            break

    def do_colosseum_actions(self):
        self.char9.greet_player()

        while True:
            interact_choice = self.textUI.get_user_input(
                f"Do you want to interact with {self.char9.character_name}? (yes/no): ").lower()

            if interact_choice == "yes":
                self.interact_with_character_swap('char9')
            elif interact_choice == "no":
                pass
            else:
                self.textUI.print_to_textUI("Don't know what you mean. Please enter 'yes' or 'no'.")
                continue
            colosseum_speech = f"""{self.char9.character_name}: Her home city is enriched with history and culture.
Home of the Ottoman Empire. I thought it was real. I almost had her.
"""
            for char in colosseum_speech:
                print(char, end='', flush=True)
                time.sleep(0.02)
            self.display_portal_options()
            self.check_win_condition()
            break


    def check_win_condition(self):
        return (self.char2.held_item.item_name != self.item3.item_name and
                self.char3.held_item.item_name != self.item4.item_name and
                self.char4.held_item.item_name != self.item6.item_name and
                self.char5.held_item.item_name != self.item2.item_name and
                self.char6.held_item.item_name != self.item9.item_name and
                self.char7.held_item.item_name != self.item7.item_name and
                self.char8.held_item.item_name != self.item5.item_name and
                self.char9.held_item.item_name != self.item8.item_name and
                self.char10.held_item == self.item8)


    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """
        self.player_name = input("What's your name?: ")
        print(f"Hey {self.player_name}")
        self.textUI.print_to_textUI("You just woke up in Egypt. She's waiting for you.") # Changed
        self.textUI.print_to_textUI("The one you longed for. Find her...") # Changed
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

        final_text1 = (f"""
        You just woke up in Egypt. She's waiting for you.
        The one you longed for. Find her...
        Your command words are: {self.show_command_words()}
""")
        for char in final_text1:
            print(char, end='', flush=True)
            time.sleep(0.03)

    def final_message(self):
        final_text = (f"""
        You made it... She's there... Approach her.
        *knock* *knock*
        {self.player_name} It's time for food...
        6:14pm Thursday, 14 December 2023
        location: Shutter Island
        input any character to finish.
        """)
        for char in final_text:
            print(char, end='', flush=True)
            time.sleep(0.06)

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'portal', 'quit'] # Changed

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a 2-tuple of the form (command_word, second_word)
        :return: True if the game has been quit, False otherwise
        """
        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()
            logging.info(f"User command: {command_word} {second_word if second_word else ''}")

        want_to_quit = False
        if command_word == "HELP":
            self.print_help()
        elif command_word == "PORTAL": # Changed
            self.do_go_command(second_word)
        elif command_word == "QUIT":
            want_to_quit = True
            print("BYE")
        else:
            # Unknown command...
            self.textUI.print_to_textUI("Don't know what you mean.")

        return want_to_quit


    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI("Find her. She's waiting.") # Changed
        self.textUI.print_to_textUI("You will realise soon.") # Changed
        self.textUI.print_to_textUI("Try inputting 'portal 1' ") # Changed
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}.')

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param second_word: the direction the player wishes to travel in
        :return: None
        """
        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Which Portal? portal 1?") # Changed
            return

        next_room = self.current_room.get_exit(second_word)
        print(next_room.name, second_word)
        if next_room == None:
            self.textUI.print_to_textUI("There is no door!")
        else:
            self.current_room = next_room
            self.textUI.print_to_textUI(self.current_room.get_long_description())



def main():

    game = Game()
    game.play()

if __name__ == "__main__":
    main()