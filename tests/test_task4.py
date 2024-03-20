import unittest
from ed_utils.decorators import number, visibility
from unittest.mock import patch
import random
from poke_team import *
from pokemon import *
from tower import *


class TestTower(unittest.TestCase):
    DEFAULT_SEED = 20

    def setUp(self) -> None:
        BattleTower.MIN_LIVES = 2
        BattleTower.MAX_LIVES = 10

        random.seed(TestTower.DEFAULT_SEED)
        self.player_trainer = Trainer('Ash')
        self.player_trainer.pick_team("Random")
        self.player_trainer.get_team().assemble_team(BattleMode.ROTATE)

        self.bt = BattleTower()
        self.bt.set_my_trainer(self.player_trainer)
        self.bt.generate_enemy_trainers(2)

    @number("4.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_tower(self):
        # Check number of enemies defeated
        self.assertEqual(self.bt.enemies_defeated(), 0, "Battle tower not set up correctly")
        while self.bt.battles_remaining():
            self.bt.next_battle()
        self.assertEqual(self.bt.enemies_defeated(), 16, "An issue occurred during battle")

    @number("4.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_regenerate_set(self):
        while self.bt.battles_remaining():
            self.bt.next_battle()
        self.player_trainer.get_team().regenerate_team(BattleMode.SET)
        self.assertEqual(str(self.player_trainer.get_team()[0]), "Graveler (Level 2) with 40 health and 0 experience")

    @number("4.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_regenerate_rotate(self):
        while self.bt.battles_remaining():
            self.bt.next_battle()
        self.player_trainer.get_team().regenerate_team(BattleMode.ROTATE)
        self.assertEqual(str(self.player_trainer.get_team()[0]), "Farfetchd (Level 8) with 52 health and 0 experience")

    @number("4.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_regenerate_optimise(self):
        while self.bt.battles_remaining():
            self.bt.next_battle()
        self.player_trainer.get_team().regenerate_team(BattleMode.OPTIMISE, criterion="defence")
        self.assertEqual(str(self.player_trainer.get_team()[0]), "Kingler (Level 21) with 30 health and 0 experience")

if __name__ == '__main__':
    unittest.main()
