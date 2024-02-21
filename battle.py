from poke_team import Trainer, PokeTeam
from enum import Enum
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from data_structures.array_sorted_list import ArraySortedList
from data_structures.sorted_list_adt import ListItem
from typing import Tuple


class BattleMode(Enum):
    SET = 0
    ROTATE = 1
    OPTIMISE = 2

class Battle:

    CRITERION_LIST = ["health", "experience", "defence", "battle_power", "level"]

    def __init__(self, trainer_1: Trainer, trainer_2: Trainer, battle_mode: BattleMode, criterion = "health") -> None:
        raise NotImplementedError

    def commence_battle(self) -> Trainer | None:
        raise NotImplementedError

    def _create_teams(self) -> Tuple[PokeTeam, PokeTeam]:
        raise NotImplementedError

    def set_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def rotate_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def special(self) -> None:
        raise NotImplementedError

if __name__ == '__main__':
    t1 = Trainer('Ash')
    t1.pick_team("random")

    t2 = Trainer('Gary')
    t2.pick_team('random')
    b = Battle(t1, t2, BattleMode.ROTATE)
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")
