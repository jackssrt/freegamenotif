from typing import Tuple
from modules.sources import Sources
from modules.notifs import Notifs
from modules.logs import logger


class Loader:
    @staticmethod
    def load() -> Tuple[Sources, Notifs]:
        logger.info("Gonna start loading")
        print("Loading")
        print("|   Sources")
        s = Sources()
        logger.info("Done loading Sources")
        print("|   Notifs")
        n = Notifs()
        logger.info("Done loading Notifs")
        print("Loading complete!" + "\n" * 2)
        return s, n
