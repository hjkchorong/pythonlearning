#!/usr/bin/env python3
# (c) 2018 Hyeongjin Kim
# a class file for block and Sudoku

class Block(object):
    """3x3 Block"""
    def __init__(self):
        self._block = [0 for _ in range(9)]

    def __setitem__(self, point, value):
        """Point is a tuple (row,column)"""
        assert 0 <= value <= 9, "All numbers in the block must be between 0 and 9 (inclusive)."
        # if value in self._block:
        #     raise ValueError("The value is already in block.")
        self._block[3*point[0] + point[1]] = value

    def __getitem__(self, point):
        return self._block[3*point[0] + point[1]]

    def __str__(self):
        result = ''
        for i in range(0,9):
            if i%3 == 0 and i != 0:
                result += '\n'
            result += str(self._block[i])
        return result

class Sudoku(object):
    def __init__(self):
        self._board = [Block() for _ in range(9)]
        self._values = [i for i in range(1,9+1)]
        self._points = [(row,column) for row in range(9) for column in range(9)]

    def __setitem__(self, point, value):
        assert 0 <= (point[0] and point[1]) <= 8, "The value must be inside the Sudoku board!"
        assert 0 <= value <= 9, "The value must be between 0 and 9 (inclusive)."
        block_point = (point[0]//3, point[1]//3)
        targetblock = self._board[3*block_point[0] + block_point[1]]
        targetblock[point[0]%3, point[1]%3] = value

    def __getitem__(self, point):
        block_point = (point[0]//3, point[1]//3)
        targetblock = self._board[3*block_point[0] + block_point[1]]
        return targetblock[point[0]%3, point[1]%3]

    def create(self,initial_dict):
        for key,value in initial_dict.items():
            self[key] = value

    def __str__(self):
        result = ''
        for i in range(0,3):
            result += '\n'
            for j in range(0,9):
                if j % 3 == 0 and j != 0:
                    result += '\n'
                result += str(self._board[i*3+j%3]).split('\n')[j//3]
        return result
