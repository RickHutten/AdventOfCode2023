import re
from typing import List, Dict

import numpy as np

from Data import day_two as data

Set = Dict[str, int]
Game = List[Set]
Games = Dict[int, Game]


def parse_data(raw_data: str) -> Games:
    result = {}
    for line in raw_data.split("\n"):
        game_id = int(re.search(r"Game (\d+):", line).group(1))
        game = [{p.split(" ")[1]: int(p.split(" ")[0]) for p in s.split(", ")} for s in line.split(": ")[1].split("; ")]
        result[game_id] = game
    return result


def sum_possible_games(available_cubes: Dict, games: Games) -> int:
    count = 0
    for game_id, game in games.items():
        possible = True
        for game_set in game:
            for color, amount in game_set.items():
                if available_cubes[color] < amount:
                    possible = False
        if possible:
            count += game_id
    return count


def get_min_cubes(game: Game) -> Dict:
    minimum_cubes = {"red": 0, "green": 0, "blue": 0}
    for game_set in game:
        for color, amount in game_set.items():
            if minimum_cubes[color] < amount:
                minimum_cubes[color] = amount
    return minimum_cubes


def sum_power_sets(games: Games):
    return sum([np.prod(list(get_min_cubes(game).values())) for game in games.values()])


parsed = parse_data(data.data[0])
print(sum_possible_games({"red": 12, "green": 13, "blue": 14}, parsed))
print(sum_power_sets(parsed))
