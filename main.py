from disk import Disk
from game import Game
from player import Player
from board import Board

board = Board(6, 7)
game = Game(board, 4, 2)
game.play()