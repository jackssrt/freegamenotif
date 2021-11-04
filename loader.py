from typing import Tuple
from source import Sources
from notif import Notifs
from dotenv import load_dotenv


class Loader:
    @staticmethod
    def load_env() -> None:
        load_dotenv()

    @staticmethod
    def load() -> Tuple[Sources, Notifs]:
        load_dotenv()
        print("Loading")
        print("|   Sources")
        s = Sources()
        print("|   Notifs")
        n = Notifs()
        print("Loading complete!"+"\n"*2)
        return s, n
