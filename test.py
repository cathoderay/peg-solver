#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File: test.py
    Description: testing resta1.py
"""

__author__  = "Ronald Andreu Kaiser"
__email__   = "<raios DOT catodicos AT gmail DOT com>"
__date__    = "Sep, 2012"


import unittest

import solver 


class Resta1Test(unittest.TestCase):
    def setUp(self):
        self.piece = '*'
        self.hole = 'o'
        self.blank = ' '
        self.board = solver.create_board()
    
    def test_count_one_piece(self):
        row = [self.hole]*7
        board = [row[:] for i in xrange(7)]
        board[3][3] = self.piece 
        expected = 1
        result = solver.count_pieces(board)
        self.assertEqual(expected, result)
                 
    def test_count_32_pieces_in_starting_board(self):
        board = solver.create_board()
        expected = 32
        result = solver.count_pieces(board)
        self.assertEqual(expected, result)

    def test_legal_move(self):
        board = solver.create_board()
        expected = True
        result = solver.valid_move(board, 1, 3, 'd')
        self.assertEqual(expected, result)

    def test_ilegal_move(self):
        board = solver.create_board()
        expected = False 
        result = solver.valid_move(board, 1, 3, 'u')
        self.assertEqual(expected, result)

    def test_valid_moves(self):
        board = solver.create_board()
        expected = [(1, 3, 'd'), (5, 3, 'u'),
                    (3, 1, 'r'), (3, 5, 'l')]
        result = solver.valid_moves(board)
        for x in result:
            self.assertIn(x, expected)

    def test_legal_moving(self):
        movement = (1, 3, 'd')
        expected = [[' ', ' ', '*', '*', '*', ' ', ' '],
                    [' ', ' ', '*', 'o', '*', ' ', ' '],
                    ['*', '*', '*', 'o', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*'],
                    ['*', '*', '*', '*', '*', '*', '*'],
                    [' ', ' ', '*', '*', '*', ' ', ' '],
                    [' ', ' ', '*', '*', '*', ' ', ' ']]
        solver.move(self.board, *movement)
        result = self.board
        self.assertEqual(expected, result)
       

if __name__ == "__main__":
    unittest.main()
