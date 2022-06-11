import json
import random
from typing import Any, Dict, List, Optional

import epicstore_api  # type: ignore
from modules.classes import Game

api = epicstore_api.EpicGamesStoreAPI()


def findDev(game: Dict[str, Any]) -> Optional[str]:
    for x in game["customAttributes"]:
        if x["key"] == "developerName":
            return x["value"]
    return None


def makeUrl(game: Dict[str, Any]) -> str:
    return f"https://www.epicgames.com/store/en-US/p/{game['productSlug']}"


def findThumbnail(game: Dict[str, Any]) -> str:
    for x in game["keyImages"]:
        if x["type"] == "Thumbnail":
            return x["url"]
    return random.choice(game["keyImages"])["url"]


def check() -> List[Game]:
    free_games: Dict[str, Any] = api.get_free_games()
    with open("./debugEpicgames.json", "w") as f:
        f.write(json.dumps(free_games, indent=4))
    games: List[Game] = []
    for game in free_games["data"]["Catalog"]["searchStore"]["elements"]:
        price = game["price"]["totalPrice"]
        if price["discountPrice"] == 0 and game["status"] == "ACTIVE":
            dev, url, image = (
                findDev(game),
                makeUrl(game),
                findThumbnail(game),
            )
            games.append(
                Game(game["title"], game["description"], url, image, game["id"], dev)
            )
    return games
