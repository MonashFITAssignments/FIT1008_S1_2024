import unittest
from ed_utils.decorators import number, visibility
from unittest.mock import patch
from io import StringIO
import random
from poke_team import *
from pokemon import *

class TestPokeTeam(unittest.TestCase):
    @number("2.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_selected_pokemon(self):
        poketeam = PokeTeam()
        PokeTeam.TEAM_LIMIT = 2
        poketeam.choose_randomly()
        self.assertEqual(len(poketeam), 2, "Team not being selected properly")
        PokeTeam.TEAM_LIMIT = 6

    @number("2.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_regenerate_team(self):
        poketeam = PokeTeam()
        poketeam.choose_randomly()
        poketeam.assemble_team(battle_mode=BattleMode.SET)
        poketeam.team.array[0].defend(200)
        poketeam.regenerate_team(battle_mode=BattleMode.SET)
        self.assertGreater(poketeam.team.array[0].get_health(), 0, "Regenerate team not configured properly")

    @number("2.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_internals(self):
        poketeam = PokeTeam()
        poketeam.choose_randomly()
        self.assertIsNotNone(poketeam[0], " Poketeam's __getitem__ not working correctly")

class TestTrainer(unittest.TestCase):
    @number("2.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_pick_team(self):
        trainer = Trainer('Ash')
        trainer.pick_team('Random')
        sample = PokeTeam()

        self.assertEqual(type(trainer.get_team()), type(sample), "Trainer pick_team isn't set up correctly")

    @number("2.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_get_name(self):
        trainer = Trainer('Ash')
        self.assertEqual(trainer.get_name(), 'Ash', "Trainer get_name not set up correctly")

    @number("2.6")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_get_pokedex_completion(self):
        trainer = Trainer('Ash')
        trainer.register_pokemon(Pikachu())
        trainer.register_pokemon(Pidgey())
        trainer.register_pokemon(Aerodactyl())

        self.assertEqual(trainer.get_pokedex_completion(), 0.2)

    @number("2.7")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_str(self):
        trainer = Trainer('Ash')
        trainer.register_pokemon(Pikachu())
        trainer.register_pokemon(Pidgey())
        trainer.register_pokemon(Aerodactyl())
        trainer.register_pokemon(Squirtle())
        trainer.register_pokemon(Weedle())
        trainer.register_pokemon(Meowth())
        trainer.register_pokemon(Zapdos())

        expected_str ="Trainer Ash Pokedex Completion: 40%"

        self.assertEqual(str(trainer), expected_str, "Trainer Str method is not set up correctly")


if __name__ == '__main__':
    unittest.main()
