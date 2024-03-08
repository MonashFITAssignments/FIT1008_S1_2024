import unittest
from ed_utils.decorators import number, visibility
from unittest.mock import patch
import random
from poke_team import *
from pokemon import *
from battle import *

random.seed(5)

class TestBattle(unittest.TestCase):
    @number("3.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_set_battle(self):
        t1 = Trainer('Gary')
        t2 = Trainer('Ash')

        b = Battle(t1, t2, BattleMode.SET)
        b._create_teams()
        t1.get_team().special(BattleMode.SET)
        winner = b.commence_battle()

        expected_winner = t2
        self.assertEqual(expected_winner.get_name(), winner.get_name(), "Set Mode battle failed")

    @number("3.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_rotate_battle(self):
        random.seed(20)
        t1 = Trainer('Gary')
        t2 = Trainer('Ash')

        b = Battle(t1, t2, BattleMode.ROTATE)
        b._create_teams()
        winner = b.commence_battle()

        expected_winner = t1
        self.assertEqual(expected_winner.get_name(), winner.get_name(), "Rotate Mode battle failed")
        self.assertEqual(expected_winner.get_pokedex_completion(), 0.67, "Pokedex completion not being updated in battle")


if __name__ == '__main__':
    unittest.main()
