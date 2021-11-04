import abc
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Game:
    title: str
    desc:  str
    link:  str
    image: str
    id:    str
    developer: Optional[str] = None
