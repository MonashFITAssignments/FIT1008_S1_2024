import unittest
from unittest.mock import patch
import random
from poke_team import *
from pokemon import *
from battle import *

random.seed(5)

class TestBattle(unittest.TestCase):
    def test_set_battle(self):
        t1 = Trainer('Gary')
        t2 = Trainer('Ash')

        b = Battle(t1, t2, BattleMode.SET)
        b.create_teams()
        t1.get_team().special(BattleMode.SET)
        winner = b.commence_battle()

        expected_winner = t2
        self.assertEqual(expected_winner.get_name(), winner.get_name(), "Set Mode battle failed")

    def test_rotate_battle(self):
        t1 = Trainer('Gary')
        t2 = Trainer('Ash')

        b = Battle(t1, t2, BattleMode.ROTATE)
        b.create_teams()
        winner = b.commence_battle()

        expected_winner = t1
        self.assertEqual(expected_winner.get_name(), winner.get_name(), "Rotate Mode battle failed")
        self.assertEqual(expected_winner.get_pokedex_completion(), 0.06, "Pokedex completion not being updated in battle")


if __name__ == '__main__':
    unittest.main()
