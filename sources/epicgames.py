from typing import Any, Dict, List
from classes import Game
import epicstore_api
import json
import random
api = epicstore_api.EpicGamesStoreAPI()


def findDev(game: Dict[str, Any]) -> str:
    for x in game["customAttributes"]:
        if x["key"] == "developerName":
            return x["value"]


def makeUrl(game: Dict[str, Any]) -> str:
    for x in game["catalogNs"]["mappings"]:
        if x["pageType"] == "productHome":
            return f"https://www.epicgames.com/store/en-US/p/{x['pageSlug']}"
    return f"https://www.epicgames.com/store/en-US/p/{game['urlSlug']}"


def findThumbnail(game: Dict[str, Any]) -> str:
    for x in game["keyImages"]:
        if x["type"] == "Thumbnail":
            return x["url"]
    return random.choice(game["keyImages"])


def check() -> List[Game]:
    free_games: Dict[str, Any] = api.get_free_games()
    with open("./debugEpicgames.json", "w") as f:
        f.write(json.dumps(free_games, indent=4))
    games: List[Game] = []
    for game in free_games["data"]["Catalog"]["searchStore"]["elements"]:
        price = game["price"]["totalPrice"]
        if price["discount"] != 0 and price["discountPrice"] == 0 and game["status"] == "ACTIVE":
            dev, url, image = (findDev(game), makeUrl(game),
                               findThumbnail(game),)
            games.append(Game(game["title"], game["description"],
                              url, image, game["id"], dev))
    return games
