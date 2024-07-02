from board import *
import copy
import random
from util import *

def initialize_board(width = BOARD_WIDTH, height = BOARD_HEIGHT):
    board = [[0 for x in range(width)] for y in range(height)]
    populate_board(board)
    return board

def load_board(file):
    board = [[] for i in range(BOARD_WIDTH)]
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in reversed(lines):
            row = list(map(int, line.split()))
            val = 0
            for value in row:
                board[val].append(value)
                val += 1
    return board

def populate_board(board):
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[x][y] == 0: board[x][y] = random.randint(1,5)

def refill_board(board):
    newboard = copy.deepcopy(board)
    populate_board(newboard)
    newfruits = matrix_difference(newboard, board)
    while len(has_match(newfruits)) > 0:
        newboard = copy.deepcopy(board)
        populate_board(newboard)
        newfruits = matrix_difference(newboard, board)

    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            board[x][y] = newboard[x][y]


def print_board(board):
    for y in range(BOARD_HEIGHT-1, -1, -1):
        for x in range(BOARD_WIDTH):
            value = board[x][y]
            if value < 10:
                print(f" {value} ", end="")
            else:
                print(f"{value} ", end="")
        print()

def swap_fruits(board, pos1, pos2):
    board = copy.deepcopy(board)
    x1, y1 = pos1
    x2, y2 = pos2
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
    return board

def is_valid_index(x, y):
    return x >= 0 and x < BOARD_WIDTH and y >= 0 and y < BOARD_HEIGHT

def has_match(board):
    # Bottomleft cord, fruit type, match type, score
    matches = []

    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            #horizontal 3, 4, 5
            if col <= BOARD_WIDTH - 3 and board[col][row] == board[col+1][row] == board[col+2][row] and board[col][row] and board[col][row] in FRUITS:
                matches.append(((col, row), board[col][row], 'H', 3))
            if col <= BOARD_WIDTH - 4 and board[col][row] == board[col+1][row] == board[col+2][row] == board[col+3][row] and board[col][row] in FRUITS:
                matches.append(((col, row), board[col][row], 'H', 4))
            if col <= BOARD_WIDTH - 5 and board[col][row] == board[col+1][row] == board[col+2][row] == board[col+3][row] == board[col+4][row] and board[col][row] in FRUITS:
                matches.append(((col, row), board[col][row], 'H', 5))

            # Vertical 3,4,5
            if row <= BOARD_HEIGHT - 3 and board[col][row] == board[col][row+1] == board[col][row+2] and board[col][row] in FRUITS:
                matches.append(((col, row), board[col][row], 'V', 3))
            if row <= BOARD_HEIGHT - 4 and board[col][row] == board[col][row+1] == board[col][row+2] == board[col][row+3] and board[col][row] in FRUITS:
                matches.append(((col, row), board[col][row], 'V', 4))
            if row <= BOARD_HEIGHT - 5 and board[col][row] == board[col][row+1] == board[col][row+2] == board[col][row+3] == board[col][row+4] and board[col][row] in FRUITS:
                matches.append(((col, row), board[col][row], 'V', 5))

            # L shapes
            if row <= BOARD_HEIGHT - 3 and col <= BOARD_WIDTH - 3:
                if board[col][row] == board[col+1][row] == board[col+2][row] == board[col][row+1] == board[col][row+2] and board[col][row] in FRUITS:
                    matches.append(((col, row), board[col][row], 'L1', 5))
                if board[col][row] == board[col+1][row] == board[col+2][row] == board[col+2][row+1] == board[col+2][row+2] and board[col][row] in FRUITS:
                    matches.append(((col+2, row), board[col+2][row], 'L2', 5))
                if board[col+2][row+2] == board[col+1][row+2] == board[col][row+2] == board[col+2][row+1] == board[col+2][row] and board[col+2][row+2] in FRUITS:
                    matches.append(((col+2, row+2), board[col+2][row+2], 'L3', 5))
                if board[col][row+2] == board[col+1][row+2] == board[col+2][row+2] == board[col][row+1] == board[col][row] and board[col][row] in FRUITS:
                    matches.append(((col, row+2), board[col][row+2], 'L4', 5))
    return matches

def apply_gravity(board):
    # Vertical pulldown
    # highest unmovable tile in each row
    col_blocks = dict()
    for i in range(BOARD_WIDTH):
        col_blocks[i] = -1

    for col in range(BOARD_WIDTH):
        cur = 0
        for row in range(BOARD_HEIGHT): # Everything droppable falls to the bottom
            if board[col][row] >= FRUIT_KIWI and board[col][row] <= RAINBOW:
                board[col][cur], board[col][row] = board[col][row], board[col][cur]
                cur += 1
            elif board[col][row] > RAINBOW: #unmovable tile
                cur = row+1
                col_blocks[col] = row
    # # Slide down

    for row in range(BOARD_HEIGHT-1, -1, -1): #find highest fruit
        col_queue = list(range(BOARD_WIDTH)) 
        random.shuffle(col_queue)
        for col in col_queue:
            if board[col][row] in FRUITS: #if it is a fruit
                lr = [col-1, col+1]
                random.shuffle(lr)
                for col2 in lr: #pick left or right randomly
                    if not is_valid_index(col2, row-1): continue
                    if board[col2][row-1] == 0 and row-1 < col_blocks[col2]: #empty spot covered by unmoving tile
                        board[col][row], board[col2][row-1] = board[col2][row-1], board[col][row] #swap
                        landing = row-1
                        while is_valid_index(col2, landing-1):
                            if board[col2][landing-1] == 0:
                                landing -= 1
                            else:
                                break
                        board[col2][row-1], board[col2][landing] = board[col2][landing], board[col2][row-1]
                        break
                
                        
            
        


            
def get_valid_moves(board):
    moves = []
    for row in range(BOARD_HEIGHT-1):
        for col in range(BOARD_WIDTH-1):
            if board[col][row] not in FRUITS:
                continue
            if len(has_match(swap_fruits(board, (col, row), (col+1,row)))) > 0:
                moves.append(((col, row), (col + 1, row)))
            if len(has_match(swap_fruits(board, (col, row), (col,row+1)))) > 0:
                moves.append(((col, row), (col, row+1)))
    return moves
                

                
