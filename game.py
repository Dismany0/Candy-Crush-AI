from board import *
from random import randint

def initialize_board(width = BOARD_WIDTH, height = BOARD_HEIGHT):
    board = [[0 for x in range(width)] for y in range(height)]
    return board

def populate_board(board):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            board[y][x] = randint(1, 5)

def print_board(board):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            print(board[y][x], end = " ")
        print()

def drop_fruits(board):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            board[y][x] = randint(1, 5)

# this is not a deep copy
def swap_fruits(board, pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    board[y1][x1], board[y2][x2] = board[y2][x2], board[y1][x1]

def is_valid_index(x, y):
    return x >= 0 and x < BOARD_WIDTH and y >= 0 and y < BOARD_HEIGHT

def has_match(board):
    matches = []
    for row in range(BOARD_WIDTH):
        for col in range(BOARD_HEIGHT):
            # horizontal 3
            if col <= BOARD_HEIGHT - 3 and board[row][col] == board[row][col + 1] == board[row][col + 2]:
                matches.append((col, row, board[row][col], 'h', 3))
            # horizontal 4
            if col <= BOARD_HEIGHT - 4 and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                matches.append((col, row, board[row][col], 'h', 4))
            # horizontal 5
            if col <= BOARD_HEIGHT - 5 and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == board[row][col + 4]:
                matches.append((col, row, board[row][col], 'h', 5))

            # vertical 3
            if row <= BOARD_WIDTH - 3 and board[row][col] == board[row + 1][col] == board[row + 2][col]:
                matches.append((col, row, board[row][col], 'v', 3))
            # vertical 4
            if row <= BOARD_WIDTH - 4 and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                matches.append((col, row, board[row][col], 'v', 4))
            # vertical 5
            if row <= BOARD_WIDTH - 5 and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == board[row + 4][col]:
                matches.append((col, row, board[row][col], 'v', 5))

            # L shape
            # if row <= BOARD_HEIGHT - 3 and col <= BOARD_WIDTH -3:
            #     if (board[row][col] == board[row+1][col] == board[row+2][col] == board[row][col+1] == board[row][col+2] or
            #             board[row][col] == board[row+1][col] == board[row+2][col] == board[row+1][col+1] == board[row+1][col+2] or
            #             board[row][col] == board[row][col+1] == board[row][col+2] == board[row+1][col] == board[row+2][col] or
            #             board[row][col] == board[row][col+1] == board[row][col+2] == board[row+1][col+1] == board[row+2][col+1]):
            #             matches.append((row, col, board[row][col], 'l', 5))
    return matches

            
                
