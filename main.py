from modules.env import env
from modules.loader import Loader
from modules.logs import logger
import time
import os

from modules.ratelimit import ratelimit


def main():
    ratelimit.ratelimit()
    print(
        """
  __                                                      _   _  __ 
 / _|                                                    | | (_)/ _|
| |_ _ __ ___  ___  __ _  __ _ _ __ ___   ___ _ __   ___ | |_ _| |_ 
|  _| '__/ _ \/ _ \/ _` |/ _` | '_ ` _ \ / _ \ '_ \ / _ \| __| |  _|
| | | | |  __/  __/ (_| | (_| | | | | | |  __/ | | | (_) | |_| | |  
|_| |_|  \___|\___|\__, |\__,_|_| |_| |_|\___|_| |_|\___/ \__|_|_|  
                    __/ |                                           
                   |___/                                            
"""
    )
    s, n = Loader.load()
    print("Running")
    games = s.check()
    n.notify(games)
    ratelimit.lastRan = time.time()


if __name__ == "__main__":
    logger.info("==================")
    logger.info("==== STARTING ====")
    logger.info("==================")
    if env.FGN_WEB:
        logger.info("Starting in web mode")
        import modules.web

        modules.web.main()
    else:
        logger.info("Starting normally")
        main()
