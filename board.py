from disk import Disk

class Board:
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        self._board = None
        self.InitBoard()

    def InitBoard(self):
        self._board = [[Disk.EMPTY for _ in range(self._cols)] for _ in range(self._rows)]
    
    def DisplayBoard(self):
        return self._board
    
    def GetRows(self):
        return self._rows
    
    def GetColumns(self):
        return self._cols
    
    def placePiece(self, column, disk):
        if column < 0 or column >= self._cols:
            raise ValueError('Invalid column')
        if disk == Disk.EMPTY:
            raise ValueError('Invalid disk')
        for row in range(self._rows-1, -1, -1):
            if self._board[row][column] == Disk.EMPTY:
                self._board[row][column] = disk
                return row

    def checkWin(self, connectN, row, col, disk):
        count = 0
        # Check horizontal
        for c in range(self._cols):
            if self._board[row][c] == disk:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check vertical
        count = 0
        for r in range(self._rows):
            if self._board[r][col] == disk:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check diagonal
        count = 0
        for r in range(self._rows):
            c = row + col - r
            if c >= 0 and c < self._cols and self._board[r][c] == disk:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(self._rows):
            c = col - row + r
            if c >= 0 and c < self._cols and self._board[r][c] == disk:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        return False
    
