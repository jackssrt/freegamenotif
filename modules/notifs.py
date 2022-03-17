from typing import Any, Dict, List
from modules.classes import Game
from modules.logs import discordlog, logger
from modules.env import env
import importlib
import os
import json

directory = "./notifs"


class Notifs:
    notifiedGames: List[str]
    modules: Dict[str, Any]

    def __init__(self) -> None:

        self.modules = {}
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if not os.path.isfile(filepath):
                continue
            logger.info(f"Loading Notif {filename}")

            modulename = os.path.splitext(filename)[0]

            module = importlib.import_module(f"notifs.{modulename}")
            self.modules[filename] = module
            logger.info(f"Loaded Notif {filename}")
            print(f"|   |   {filename} loaded!")
        # Load notified.json
        if not os.path.exists("./notified.json"):
            logger.info("Notified.json doesnt exist, creating it...")
            discordlog("Notified.json doesnt exist, creating it...")
            with open("./notified.json", "w") as f:
                f.write("[]")
            self.notifiedGames = []
            logger.info(
                f"Created notified.json @ {os.path.realpath('./notified.json')}"
            )
        else:
            logger.info("Reading notified.json")
            with open("./notified.json") as f:
                self.notifiedGames = json.load(f)
            discordlog(f"notifiedGames loaded with val {self.notifiedGames}")
            logger.info("Read notified.json and loaded it")

    def notify(self, games: List[Game]):
        """Notifies a list of games using all notifs"""
        print("|   Notifying")
        for module_name in self.modules.keys():
            print(f"|   |   {module_name}")
            for game in games:
                logger.info(f"Game: {game}")
                if env.FGN_FORCE or not (game.id in self.notifiedGames):
                    logger.info(
                        f"Notifing because env FGN_FORCE is {env.FGN_FORCE} and game.id in notified is {game.id in self.notifiedGames}"
                    )
                    discordlog(
                        f"Notifing because env FGN_FORCE is {env.FGN_FORCE} and game.id in notified is {game.id in self.notifiedGames}\nnotified games: {self.notifiedGames}"
                    )
                    print(f"|   |   |   {game.title}")
                    self.modules[module_name].notify(game)
        for game in games:
            if not (game.id in self.notifiedGames):
                logger.info(f"Adding {game} into notified")
                self.notifiedGames.append(game.id)
        # Save notified.json
        with open("./notified.json", "w") as f:
            json.dump(self.notifiedGames, f, indent=4)
            logger.info(f"Saved notified.json with val: {self.notifiedGames}")
