from board import *
from game import *
from random import *

#set seed to 0


board = initialize_board()
populate_board(board)
print_board(board)
print(has_match(board))