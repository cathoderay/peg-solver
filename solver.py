#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: solver.py
    Description: Peg solitaire solver for english board:

        * * *
        * * *
    * * * * * * *
    * * * o * * *
    * * * * * * *
        * * *
        * * *
"""
__author__  = "Ronald Andreu Kaiser"
__email__   = "<raios DOT catodicos AT gmail DOT com>"
__date__    = "Sep, 2012"


import pprint
import copy


PIECE = '*'
HOLE = 'o'
BLANK = ' '


def create_board():
    row = [PIECE for i in range(7)]
    m = [row[:] for j in range(7)]
    invalid = [(0, 0), (0, 1), (1, 0), (1, 1),
               (5, 0), (5, 1), (6, 0), (6, 1),
               (0, 5), (0, 6), (1, 5), (1, 6),
               (5, 5), (5, 6), (6, 5), (6, 6)]
    for x, y in invalid:
        m[x][y] = BLANK
    m[3][3] = HOLE
    return m


def valid_move(m, x, y, d):
    if not m[x][y] == PIECE: return False
    if d == 'l' and y > 1 and m[x][y-1] == PIECE and m[x][y-2] == HOLE or \
       d == 'r' and y < 5 and m[x][y+1] == PIECE and m[x][y+2] == HOLE or \
       d == 'u' and x > 1 and m[x-1][y] == PIECE and m[x-2][y] == HOLE or \
       d == 'd' and x < 5 and m[x+1][y] == PIECE and m[x+2][y] == HOLE:
       return True
    return False


def move(m, x, y, d):
    m[x][y] = HOLE
    if d == 'l':
        m[x][y-1] = HOLE
        m[x][y-2] = PIECE
    if d == 'r':
        m[x][y+1] = HOLE
        m[x][y+2] = PIECE
    if d == 'u':
        m[x-1][y] = HOLE
        m[x-2][y] = PIECE
    if d == 'd':
        m[x+1][y] = HOLE
        m[x+2][y] = PIECE


def valid_moves(m):
    return [(x, y, d)
            for x in range(7)
            for y in range(7)
            for d in ['l', 'r', 'u', 'd']
                if valid_move(m, x, y, d)]


def count_pieces(m):
    return len([m[i][j] for i in range(7)
                        for j in range(7)
                            if m[i][j] == PIECE])


def solved(m):
    return count_pieces(m) == 1


def play(m, solution):
    if solved(m):
        return True

    to_test = valid_moves(m)
    for t in to_test:
        m_copy = copy.deepcopy(m)
        move(m_copy, *t)
        if play(m_copy, solution):
            solution.append(t)
            return True
    return False


if __name__ == '__main__':
    board = create_board()
    solution = []
    play(board, solution)
    solution.reverse()
    pprint.pprint(solution)
