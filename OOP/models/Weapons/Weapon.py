from object_types import Stats
class Weapon:
    def __init__(self, name: str ,stats: Stats):
        self.__name = name
        self._attack = stats['attack']
        self._defense= stats['defence']  if stats['defence'] else 0.0
        self._speed = stats['speed'] if stats['speed'] else 0.0
