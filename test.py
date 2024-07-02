from board import *
from game import *
from random import *
import time

#set seed to 0
# seed(0)

# start = time.time()

# for i in range (1000):
#     board = initialize_board()

#     while(len(has_match(board)) > 0):
#         board = initialize_board()

#     # print_board(board)
#     # print(get_valid_moves(board))
# print(f"Elapsed time: {time.time() - start} seconds")

board = load_board("input.txt")
refill_board(board)
print_board(board)
print(has_match(board))
# print(get_valid_moves(board))

# apply_gravity(board)
# print_board(board)