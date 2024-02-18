import enum

class Player:
    def __init__(self, name: str, color: enum):
        self._name = name
        self._color = color

    def GetName(self):
        return self._name
    
    def GetColor(self):
        return self._color