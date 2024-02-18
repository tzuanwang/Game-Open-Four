import enum

class Player:
    def __init__(self, name: str, color: enum):
        self._name = name
        self._color = color

    @property
    def GetName(self):
        return self._name
    
    @property
    def GetColor(self):
        return self._color