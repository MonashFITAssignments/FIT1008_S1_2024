from pokemon import *
import random
from typing import List
from battle_mode import BattleMode

class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = None # change None value if necessary
        self.team_count = 0

    def choose_manually(self):
        raise NotImplementedError

    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team[i] = all_pokemon[rand_int]()
            self.team_count += 1

    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None:
        raise NotImplementedError

    def assign_team(self, criterion: str = None) -> None:
        raise NotImplementedError

    def assemble_team(self, battle_mode: BattleMode) -> None:
        raise NotImplementedError

    def special(self, battle_mode: BattleMode) -> None:
        raise NotImplementedError

    def __getitem__(self, index: int):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class Trainer:

    def __init__(self, name) -> None:
        raise NotImplementedError

    def pick_team(self, method: str) -> None:
        raise NotImplementedError

    def get_team(self) -> PokeTeam:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def register_pokemon(self, pokemon: Pokemon) -> None:
        raise NotImplementedError

    def get_pokedex_completion(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())
