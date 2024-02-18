from disk import Disk
from game import Game
from player import Player
from board import Board

board = Board(7, 8)
game = Game(board, 6, 2)
game.play()