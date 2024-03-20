import unittest
from ed_utils.decorators import number, visibility
from unittest.mock import patch
import random
from poke_team import *
from pokemon import *
from battle import *
from typing import Tuple


class TestBattle(unittest.TestCase):
    DEFAULT_SEED: int = 20

    def setUp(self) -> None:
        self.trainer1 = Trainer('Gary')
        self.trainer2 = Trainer('Ash')

    def __create_teams(self, battle_mode: BattleMode, criterion: str = "health") -> Battle:
        random.seed(TestBattle.DEFAULT_SEED)
        battle = Battle(self.trainer1, self.trainer2, battle_mode, criterion=criterion)
        battle._create_teams()
        return battle

    def __test_set_battle(self) -> Tuple[Trainer, Trainer]:
        battle = self.__create_teams(BattleMode.SET)
        self.trainer1.get_team().special(BattleMode.SET)
        return battle.commence_battle(), self.trainer2

    def __test_rotate_battle(self) -> Tuple[Trainer, Trainer]:
        battle = self.__create_teams(BattleMode.ROTATE)
        return battle.commence_battle(), self.trainer2

    def __test_optimise_battle(self) -> Tuple[Trainer, Trainer]:
        # Note: this should create a team in ascending order, where the criterion is their current health
        battle = self.__create_teams(BattleMode.OPTIMISE, "health")
        return battle.commence_battle(), self.trainer1

    @number("3.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_set_battle_result(self):
        winner, expected_winner = self.__test_set_battle()
        # Check winner (Ash's team)
        self.assertEqual(expected_winner.get_name(), winner.get_name(), f"Set Mode battle failed - {expected_winner.get_name()} should win")

    @number("3.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_set_battle_pokedex_completion(self):
        _, _ = self.__test_set_battle()
        # Check trainer's Pokedex completion (2 decimal places)
        self.assertEqual(self.trainer1.get_pokedex_completion(), 0.6, f"{self.trainer1.get_name()} - Pokedex completion not being update correctly in set battle")
        self.assertEqual(self.trainer2.get_pokedex_completion(), 0.67, f"{self.trainer2.get_name()} - Pokedex completion not being update correctly in set battle")


    @number("3.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_set_battle_team_structure(self):
        _, _ = self.__test_set_battle()

        # Check Ash's team size is 2 and that Ash has these 2 Pokemon left
        self.assertEqual(len(self.trainer2.get_team()), 2, f"{self.trainer2.get_name()} should have 2 pokemon left in their team")
        self.assertEqual(str(self.trainer2.get_team()[0]), "Pinsir (Level 5) with 22.0 health and 0 experience")
        self.assertEqual(str(self.trainer2.get_team()[1]), "Bellsprout (Level 1) with 50 health and 0 experience")

        # Check loser (Gary's team)
        self.assertEqual(len(self.trainer1.get_team()), 0, f"{self.trainer1.get_name()} should have no Pokemon left in their team")

    @number("3.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_rotate_battle_result(self):
        winner, expected_winner = self.__test_rotate_battle()
        # Check winner (Ash's team)
        self.assertEqual(expected_winner.get_name(), winner.get_name(), f"Rotate battle failed - {expected_winner.get_name()} should win")

    @number("3.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_rotate_battle_pokedex_completion(self):
        _, _ = self.__test_rotate_battle()

        # Check trainer's Pokedex completion (2 decimal places)
        self.assertEqual(self.trainer1.get_pokedex_completion(), 0.67, f"{self.trainer1.get_name()} - Pokedex completion not being update correctly in rotate battle")
        self.assertEqual(self.trainer2.get_pokedex_completion(), 0.67, f"{self.trainer2.get_name()} - Pokedex completion not being update correctly in rotate battle")

    @number("3.6")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_rotate_battle_team_structure(self):
        _, _ = self.__test_rotate_battle()

        # Check winner (Ash's team)
        self.assertEqual(len(self.trainer2.get_team()), 4, f"{self.trainer2.get_name()} should have 4 pokemon left in their team")
        self.assertEqual(str(self.trainer2.get_team()[0]), "Dragonite (Level 3) with 57.375 health and 0 experience")
        self.assertEqual(str(self.trainer2.get_team()[1]), "Weepinbell (Level 2) with 41.0 health and 0 experience")
        self.assertEqual(str(self.trainer2.get_team()[2]), "Pinsir (Level 2) with 49.0 health and 0 experience")
        self.assertEqual(str(self.trainer2.get_team()[3]), "Pinsir (Level 3) with 47.0 health and 0 experience")

        # Check loser (Gary's team)
        self.assertEqual(len(self.trainer1.get_team()), 0, f"{self.trainer1.get_name()} should have no Pokemon left in their team")

    @number("3.7")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_optimise_special(self):
        # Note: this should create a team in ascending order, where the criterion is their current health
        _ = self.__create_teams(BattleMode.OPTIMISE, "health")
        # After applying special: means the Pokemon with the highest HP will fight first
        self.trainer1.get_team().special(BattleMode.OPTIMISE)
        # Now Gary's Pokemon are in descending order, this means the Pokemon with the highest HP will fight first
        self.assertEqual(str(self.trainer1.get_team()[0]), "Farfetchd (Level 1) with 52 health and 0 experience")

    @number("3.8")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_optimise_result(self):
        winner, expected_winner = self.__test_optimise_battle()
        self.assertEqual(expected_winner.get_name(), winner.get_name(), f"Optimise battle failed - {expected_winner.get_name()} should win")

    @number("3.9")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_optimise_pokedex_completion(self):
        _, _ = self.__test_optimise_battle()
        # Check trainer's Pokedex completion (2 decimal places)
        self.assertEqual(self.trainer1.get_pokedex_completion(), 0.67, f"{self.trainer1.get_name()} - Pokedex completion not being update correctly in battle")
        self.assertEqual(self.trainer2.get_pokedex_completion(), 0.53, f"{self.trainer2.get_name()} - Pokedex completion not being update correctly in battle")

    @number("3.10")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_optimise_team_structure(self):
        _, _ = self.__test_optimise_battle()

        # Check winner (Gary's team)
        self.assertEqual(len(self.trainer1.get_team()), 5, f"{self.trainer1.get_name()} should have 5 pokemon left in their team")
        self.assertEqual(str(self.trainer1.get_team()[0]), "Dodrio (Level 5) with 7.0 health and 0 experience")
        self.assertEqual(str(self.trainer1.get_team()[1]), "Geodude (Level 1) with 40 health and 0 experience")
        self.assertEqual(str(self.trainer1.get_team()[2]), "Meowth (Level 1) with 40 health and 0 experience")
        self.assertEqual(str(self.trainer1.get_team()[3]), "Ninetales (Level 2) with 51.75 health and 0 experience")
        self.assertEqual(str(self.trainer1.get_team()[4]), "Farfetchd (Level 1) with 52 health and 0 experience")

        # Check loser (Ash's team) - We got Ash!
        self.assertEqual(len(self.trainer2.get_team()), 0, f"{self.trainer2.get_name()} should have no Pokemon left in their team")


if __name__ == '__main__':
    unittest.main()
