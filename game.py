import enum

from disk import Disk
from board import Board
from player import Player

class Game:
    def __init__(self, board, connectN, targetScore):
        self._board = board
        self._connectN = connectN
        self._targetScore = targetScore

        self._players = [
            Player('Player 1', Disk.YELLOW),
            Player('Player 2', Disk.RED)
        ]

        self._score = {}
        for player in self._players:
            self._score[player.GetName()] = 0
    

    def printBoard(self):
        print('Board:\n')
        board = self._board.DisplayBoard()
        for i in range(len(board)):
            row = ''
            for piece in board[i]:
                if piece == Disk.EMPTY:
                    row += '0 '
                elif piece == Disk.YELLOW:
                    row += 'Y '
                elif piece == Disk.RED:
                    row += 'R '
            print(row)
        print('')

    def playMove(self, player):
        self.printBoard()
        print(f"▶️ It's {player.GetName()}'s turn!")
        colCnt = self._board.GetColumns()
        moveColumn = int(input(f"Enter column between {0} and {colCnt - 1} to add disk: "))
        moveRow = self._board.placePiece(moveColumn, player.GetColor())
        return (moveRow, moveColumn)

    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.GetColor()
                if self._board.checkWin(self._connectN, row, col, pieceColor):
                    self._score[player.GetName()] += 1
                    return player

    def play(self):
        maxScore = 0
        winner = None
        while maxScore < self._targetScore:
            winner = self.playRound()
            print(f"{winner.GetName()} won the round")
            maxScore = max(self._score[winner.getName()], maxScore)

            self._board.InitBoard() # reset grid
        print(f"{winner.GetName()} won the game")
