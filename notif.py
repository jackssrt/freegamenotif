from typing import Any, Dict, List
from classes import Game
import importlib
import os
import json
directory = './notifs'


class Notifs:
    notifiedGames: list[str]
    modules: list[Any]

    def __init__(self) -> None:

        self.modules: Dict[str, Any] = {}
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if not os.path.isfile(filepath):
                continue
            print(f"|   |   {filename} loaded!")
            modulename = os.path.splitext(filename)[0]

            module = importlib.import_module(f'notifs.{modulename}')
            self.modules[filename] = module
        # Load notified.json
        if not os.path.exists("./notified.json"):
            with open("./notified.json", "w") as f:
                f.write("[]")
            self.notifiedGames = []
        else:
            with open("./notified.json") as f:
                self.notifiedGames = json.load(f)

    def notify(self, games: List[Game]):
        """Notifies a list of games using all notifs"""
        print("|   Notifying")
        for module_name in self.modules.keys():
            print(f"|   |   {module_name}")
            for game in games:
                if os.getenv("FGN_FORCE", "false") == "true" or not (game.id in self.notifiedGames):
                    print(f"|   |   |   {game.title}")
                    self.modules[module_name].notify(game)
        for game in games:
            if not (game.id in self.notifiedGames):
                self.notifiedGames.append(game.id)
        # Save notified.json
        with open("./notified.json", "w") as f:
            json.dump(self.notifiedGames, f, indent=4)
