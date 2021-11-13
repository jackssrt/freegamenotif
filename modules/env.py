import os
from typing import Any, Dict, Optional
from dotenv import load_dotenv
from modules.logs import logger

load_dotenv()


class Env:
    _cache: Dict[str, Any] = {}

    def _getBool(self, key: str) -> bool:
        "Gets a bool value from env"
        if not self._cache.get(key):
            self._cache[key] = os.getenv(key, "false").casefold().strip() == "true"
        return self._cache.get(key)

    @property
    def FGN_FORCE(self) -> bool:
        "Indicates if fgn should ignore already notified games and notify them anyway. Used for development."
        logger.info("Getting value of env FGN_FORCE")
        return self._getBool("FGN_FORCE")

    @property
    def FGN_WEB(self) -> bool:
        "Indicates if fgn should start a web server on port 8080. Used for automatic running."
        logger.info("Getting value of env FGN_WEB")
        return self._getBool("FGN_WEB")

    @property
    def FGN_DISCORD_URL(self) -> Optional[str]:
        "The discord webhook to send to."
        logger.info("Getting value of env FGN_DISCORD_URL")
        if not self._cache.get("FGN_DISCORD_URL"):
            self._cache["FGN_DISCORD_URL"] = os.getenv("FGN_DISCORD_URL").strip()
        return self._cache["FGN_DISCORD_URL"]


env = Env()
