'''
A board is a NxN numpy array.
A Coordinate is a tuple index into the board.
A Move is a (Coordinate c | None).
A PlayerMove is a (Color, Move) tuple

(0, 0) is considered to be the upper left corner of the board, and (19, 0) is the lower left.
'''
from collections import namedtuple
import copy
import itertools

import numpy as np

# Represent a board as a numpy array, with 0 empty, 1 is black, -1 is white.
# This means that swapping colors is as simple as multiplying array by -1.
WHITE, EMPTY, BLACK, UNKNOW = range(-1, 3)

class PlayerMove(namedtuple('PlayerMove', ['color', 'move'])): pass

# these are initialized by set_board_size
N = None
ALL_COORDS = []
EMPTY_BOARD = None
NEIGHBORS = {}
DIAGONALS = {}

def set_board_size(n):
    '''
    Hopefully nobody tries to run both 9x9 and 19x19 game instances at once.
    Also, never do "from go import N, W, ALL_COORDS, EMPTY_BOARD".
    '''
    global N, ALL_COORDS, EMPTY_BOARD, NEIGHBORS, DIAGONALS
    if N == n: return
    N = n
    ALL_COORDS = [(i, j) for i in range(n) for j in range(n)]
    EMPTY_BOARD = np.zeros([n, n], dtype=np.int8)
    def check_bounds(c):
        return c[0] % n == c[0] and c[1] % n == c[1]

    NEIGHBORS = {(x, y): list(filter(check_bounds, [(x+1, y), (x-1, y), (x, y+1), (x, y-1)])) for x, y in ALL_COORDS}
    DIAGONALS = {(x, y): list(filter(check_bounds, [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)])) for x, y in ALL_COORDS}

def place_stones(board, color, stones):
    for s in stones:
        board[s] = color

class Position():
    def __init__(self, board=None, n=0, caps=(0, 0), recent=tuple(), to_play=BLACK):
        '''
        board: a numpy array
        n: an int representing moves played so far
        caps: a (int, int) tuple of captures for B, W.
        recent: a tuple of PlayerMoves, such that recent[-1] is the last move.
        to_play: BLACK or WHITE
        '''
        self.board = board if board is not None else np.copy(EMPTY_BOARD)
        self.n = n
        self.caps = caps
        self.recent = recent
        self.to_play = to_play

    def __deepcopy__(self, memodict={}):
        new_board = np.copy(self.board)
        return Position(new_board, self.n, self.caps,self.recent, self.to_play)

    def __str__(self):
        pretty_print_map = {
            WHITE: '\x1b[0;31;47mO',
            EMPTY: '\x1b[0;31;43m.',
            BLACK: '\x1b[0;31;40mX',
        }
        board = np.copy(self.board)
        captures = self.caps
        raw_board_contents = []
        for i in range(N):
            row = []
            for j in range(N):
                appended = '<' if (self.recent and (i, j) == self.recent[-1].move) else ' '
                row.append(pretty_print_map[board[i,j]] + appended)
                row.append('\x1b[0m')
            raw_board_contents.append(''.join(row))

        row_labels = ['%2d ' % i for i in range(N, 0, -1)]
        annotated_board_contents = [''.join(r) for r in zip(row_labels, raw_board_contents, row_labels)]
        header_footer_rows = ['   ' + ' '.join('ABCDEFGHJKLMNOPQRST'[:N]) + '   ']
        annotated_board = '\n'.join(itertools.chain(header_footer_rows, annotated_board_contents, header_footer_rows))
        details = "\nMove: {}. Captures X: {} O: {}\n".format(self.n, *captures)
        return annotated_board + details

    def pass_move(self, mutate=False):
        pos = self if mutate else copy.deepcopy(self)
        pos.n += 1
        pos.recent += (PlayerMove(pos.to_play, None),)
        pos.to_play *= -1
        pos.ko = None
        return pos

    def flip_playerturn(self, mutate=False):
        pos = self if mutate else copy.deepcopy(self)
        pos.ko = None
        pos.to_play *= -1
        return pos

    def play_move(self, c, color=None, mutate=False):
        if color is None:
            color = self.to_play
        pos = self if mutate else copy.deepcopy(self)
        if c is None:
            pos = pos.pass_move(mutate=mutate)
            return pos

        place_stones(pos.board, color, [c])
        #captured_stones = pos.add_stone(color, c)
        #place_stones(pos.board, EMPTY, captured_stones)
        opp_color = color * -1
        pos.n += 1
        pos.recent += (PlayerMove(color, c),)
        pos.to_play *= -1
        return pos

set_board_size(21)