import logging

LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"
logging.basicConfig(filename="debug.log", level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger()
