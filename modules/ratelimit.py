import os
from time import time

from modules.logs import logger


class Ratelimit:
    _lastRan: float

    def __init__(self) -> None:
        logger.info("initing Ratelimit")
        if not os.path.exists("./lastRan.txt"):
            logger.info(
                f"{os.path.abspath('./lastRan.txt')} doesnt exist, creating it..."
            )
            with open("./lastRan.txt", "w") as f:
                f.write("0")
                self._lastRan = 0
            logger.info("Created ./lastRan.txt")
        else:
            logger.info("Loading ./lastRan.txt")
            with open("./lastRan.txt") as f:
                self._lastRan = float(f.read().strip())

    @property
    def lastRan(self) -> float:
        return self._lastRan

    @lastRan.setter
    def lastRan(self, v: float):
        logger.info("Seting lastRan and saving it")
        if isinstance(v, float):
            self._lastRan = v
            with open("./lastRan.txt", "w") as f:
                f.write(str(v))
        else:
            logger.warn("Tried to set lastRan to a non float")
            raise TypeError("Tried to set lastRan to a non float")

    def ratelimit(self):
        logger.info("Ratelimiting...")
        if time() < self.lastRan + 15:
            logger.info(f"Ratelimited try again in {self.lastRan + 15 - time()}")
            print(f"Ratelimited try again in {self.lastRan + 15 - time()}")
            exit()


ratelimit = Ratelimit()
