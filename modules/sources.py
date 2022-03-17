from typing import Any, Dict, List
from modules.classes import Game
import importlib
import os

directory = "./sources"


class Sources:
    modules: Dict[str,Any]

    def __init__(self) -> None:

        self.modules = {}
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if not os.path.isfile(filepath):
                continue
            print(f"|   |   {filename} loaded!")
            modulename = os.path.splitext(filename)[0]

            module = importlib.import_module(f"sources.{modulename}")
            self.modules[filename] = module

    def check(self):
        print("|   Checking")
        for module_name in self.modules.keys():
            print(f"|   |   {module_name}")
            games: List[Game] = []
            for game in self.modules[module_name].check():
                game: Game = game
                print(f"|   |   |   {game.title}")
                games.append(game)
            return games
