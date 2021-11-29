import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("hearts", 1)
        self.card_2 = Card("spades", 4)
        self.card_3 = Card("clubs", 9)
        self.card_4 = Card("diamonds", 7)

        self.card_game = CardGame

        self.cards = [self.card_1, self.card_2, self.card_3, self.card_4]

    def test_card_has_suit(self):
        self.assertEqual("hearts", self.card_1.suit)
    
    def test_card_has_value(self):
        self.assertEqual(4, self.card_2.value)

    def test_check_for_ace_func_works_pass(self):
        self.assertEqual(True, self.card_game.check_for_ace(self, self.card_1))
    
    def test_check_for_ace_func_works_fail(self):
        self.assertEqual(False, self.card_game.check_for_ace(self, self.card_2))

    def test_highest_card_func(self):
        self.assertEqual(self.card_3, self.card_game.highest_card(self, self.card_3, self.card_4))

    def test_cards_total_function(self):
        self.assertEqual(21, self.card_game.cards_total(self, self.cards))

    