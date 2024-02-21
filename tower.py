from poke_team import Trainer, PokeTeam
from enum import Enum
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from data_structures.array_sorted_list import ArraySortedList
from data_structures.sorted_list_adt import ListItem
from typing import Tuple

class BattleTower:
    def __init__(self) -> None:
        raise NotImplementedError

    def set_my_team(self) -> None:
        raise NotImplementedError

    def generate_teams(self) -> None:
        raise NotImplementedError

    def battles_remaining(self) -> bool:
        raise NotImplementedError

    def next_battle(self) -> Tuple[Trainer, PokeTeam, int, int]:
        raise NotImplementedError

    def enemies_defeated(self) -> int:
        raise NotImplementedError