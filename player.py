import enum

class Player:
    def __init__(self, name: str, diskColor: enum):
        self._name = name
        self._diskColor = diskColor

    @property
    def getName(self):
        return self._name
    
    @property
    def getDiskColor(self):
        return self._diskColor