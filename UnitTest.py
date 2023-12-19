import UnitTest
from backpack import *
from characters import *
from hangman import *
from room import *
from text_ui import *
from GamePers import *

class MyTestCase(UnitTest.TestCase):

    def setUp(self):
        self.b1 = Backpack(6)
        self.c1 = Character
        self.h1 = HangmanGame
        self.r1 = Room
        self.t1 = TextUI
        self.g1 = Game

    def tearDown(self):
        del self.b1
        del self.c1
        del self.h1
        del self.r1
        del self.t1
        del self.g1

    def test_backpack(self):
        self.b1.add_item("cat")
        self.assertTrue(self.b1.add_item, "cat")
        self.b1.remove_item("cat")
        self.b1.check_item("cat")

    def test_characters(self):
        self.assertTrue(self.c1.greet_player)
        self.assertTrue(self.c1.change_item_held)

    def test_hangman(self):
        self.assertTrue(self.h1.display_word)
        self.assertTrue(self.h1.make_guess)

    def test_room(self):
        self.assertTrue(self.r1.set_exit)
        self.assertTrue(self.r1.get_short_description)
        self.assertTrue(self.r1.get_long_description)
        self.assertTrue(self.r1.get_exits)
        self.assertTrue(self.r1.get_exit)

    def text_ui(self):
        self.assertTrue(self.t1.get_user_input)
        self.assertTrue(self.t1.print_to_textUI)
        self.assertTrue(self.t1.get_command)

    def test_game(self):
        self.assertTrue(self.g1.create_rooms)
        self.assertTrue(self.g1.play)
        self.assertTrue(self.g1.check_win_condition)
        self.assertTrue(self.g1.game_loop)
        self.assertTrue(self.g1.check_room)
        self.assertTrue(self.g1.display_portal_options)
        self.assertTrue(self.g1.do_chichen_actions)
        self.assertTrue(self.g1.do_taj_actions)
        self.assertTrue(self.g1.do_easter_actions)
        self.assertTrue(self.g1.do_hagia_actions)
        self.assertTrue(self.g1.do_machu_actions)
        self.assertTrue(self.g1.do_colosseum_actions)
        self.assertTrue(self.g1.do_petra_actions)
        self.assertTrue(self.g1.do_pyramids_actions)
        self.assertTrue(self.g1.do_redeemer_actions)
        self.assertTrue(self.g1.do_stone_actions)
        self.assertTrue(self.g1.do_go_command)
        self.assertTrue(self.g1.final_message)
        self.assertTrue(self.g1.interact_with_character_swap)
        self.assertTrue(self.g1.print_help)
        self.assertTrue(self.g1.print_welcome)
        self.assertTrue(self.g1.process_command)
        self.assertTrue(self.g1.show_command_words)





if __name__ == '__main__':
    UnitTest.main()