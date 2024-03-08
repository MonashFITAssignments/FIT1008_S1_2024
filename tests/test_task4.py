import unittest
from ed_utils.decorators import number, visibility
from unittest.mock import patch
import random
from poke_team import *
from pokemon import *
from tower import *

random.seed(5)

class TestTower(unittest.TestCase):
    @number("4.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_tower(self):
        player_trainer = Trainer('Ash')
        player_trainer.pick_team("Random")
        player_trainer.get_team().assemble_team(BattleMode.ROTATE)

        bt = BattleTower()
        bt.set_my_trainer(player_trainer)
        bt.generate_enemy_trainers(2)

        # Check number of enemies defeated
        self.assertEqual(bt.enemies_defeated(), 0, "Battle tower not set up correctly")

if __name__ == '__main__':
    unittest.main()
