import enum

from disk import Disk
from board import Board
from player import Player

class Game:
    def __init__(self, mock_name, mock_color, rows: int, cols: int, connectN: int, targetScore: int):
        self.players = []
        self.player_init(mock_name, mock_color)
        self.board = Board(rows, cols)
        self._connectN = connectN
        self._targetScore = targetScore

    def player_init(self, mock_name, mock_color):
        for i in range(2):
            new_player = Player(mock_name[i], Disk(mock_color[i]))
            # init player
            self.players.append(new_player)
            # init player score
            self.record[new_player] = 0

    @property
    def record(self):
        return self.__record


    def game_start(self):
        while max(self.record.values()) < self.target_score:
            for player in self.players:
                row, col = self.player_move(player)
                if self.check_win(row, col, player.color):
                    print("============================== {} won the round ==============================".format(
                        player.name))
                    self.record[player] += 1
                    self.board.grid = Board.init_board(self.board.rows_size, self.board.cols_size)
                    if self.record[player] == self.target_score:
                        break

        winner = ""
        for player, point in self.record.items():
            print("{} score {} pts".format(player.name, point))
            if point == self.target_score:
                winner = player.name

        print("============================== {} win the game! ==============================".format(
            winner))

    def player_move(self, player: Player):
        """
        :param player:
        :return: row, col from new disk position
        1. only allow to place the disk at the EMPTY place
        """
        print("=======================================================================================================")
        print("Now is {} move".format(player.name))
        self.board.display_grid()
        color = player.color
        possible_cols = {}
        for col in range(len(self.board.grid[0])):
            for row in range(len(self.board.grid)):
                if self.board.grid[row][col] == Disk.EMP:
                    possible_cols[col] = row
                    break

        col_disk = int(input("Choose the column between {}".format(list(possible_cols.keys()))))
        row_disk = possible_cols[col_disk]
        self.board.grid[row_disk][col_disk] = color
        return [row_disk, col_disk]

    # check if the there is 4 same color disks in a row
    def check_win(self, row: int, col: int, color: enum):

        if (
                self.__check_vertical(row, col, color) or
                self.__check_horizon(row, col, color) or
                self.__check_diagonal(row, col, color) or
                self.__check_anti_diagonal(row, col, color)
        ):
            return True

        return False

        # check horizontal
        # counter_horizon = 1
        # leftward = col - 1

    def __check_vertical(self, row: int, col: int, color: enum):
        # check vertical
        counter_vertical = 1

        upward = row + 1
        while upward < self.board.rows_size and self.board.grid[upward][col] == color:
            counter_vertical += 1
            upward += 1

        downward = row - 1
        while downward >= 0 and self.board.grid[downward][col] == color:
            counter_vertical += 1
            downward -= 1

        if counter_vertical >= 4:
            return True
        return False

    def __check_horizon(self, row: int, col: int, color: enum):
        # check horizon
        counter_horizon = 1

        rightward = col + 1
        while rightward < self.board.cols_size and self.board.grid[row][rightward] == color:
            counter_horizon += 1
            rightward += 1

        leftward = col - 1
        while leftward >= 0 and self.board.grid[row][leftward] == color:
            counter_horizon += 1
            leftward -= 1

        if counter_horizon >= 4:
            return True
        return False

    def __check_diagonal(self, row: int, col: int, color: enum):
        # check horizon
        counter_diagonal = 1

        rightward = col + 1
        upward = row + 1
        while (
                rightward < self.board.cols_size and
                upward < self.board.rows_size and
                self.board.grid[upward][rightward] == color
        ):
            counter_diagonal += 1
            rightward += 1
            upward += 1

        leftward = col - 1
        downward = row - 1
        while (
                leftward >= 0 and
                downward >= 0 and
                self.board.grid[downward][leftward] == color
        ):
            counter_diagonal += 1
            leftward -= 1
            downward -= 1

        if counter_diagonal >= 4:
            return True
        return False

    def __check_anti_diagonal(self, row: int, col: int, color: enum):
        # check horizon
        counter_anti_diagonal = 1

        rightward = col + 1
        downward = row - 1
        while (
                rightward < self.board.cols_size and
                downward >= 0 and
                self.board.grid[downward][rightward] == color
        ):
            counter_anti_diagonal += 1
            rightward += 1
            downward -= 1

        leftward = col - 1
        upward = row + 1
        while (
                leftward >= 0 and
                upward < self.board.rows_size and
                self.board.grid[upward][leftward] == color
        ):
            counter_anti_diagonal += 1
            leftward -= 1
            upward += 1

        if counter_anti_diagonal >= 4:
            return True
        return False