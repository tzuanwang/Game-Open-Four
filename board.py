from disk import Disk

class Board:
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self.board = None
        self.InitBoard(rows, cols)

    @staticmethod
    def InitBoard(self, rows: int, cols: int):
        return [[Disk.EMPTY for _ in range(self._cols)] for _ in range(self._rows)]
    
    
    def DisplayBoard(self):
        for row in range(len(self.board)-1,-1,-1):
            print(self.board[row])
    
    @property
    def GetRows(self):
        return self._rows
    
    @property
    def GetColumns(self):
        return self._cols
    
