#!/usr/bin/env python3
# (c) 2018 Hyeongjin Kim
# a class file for block and Sudoku

class Block(object):
    """3x3 Block"""
    def __init__(self):
        self._block = [0 for _ in range(9)]
        self._values = [i for i in range(1,10)]

    @property
    def block(self):
        return self._block

    def __setitem__(self, point, value):
        """Point is a tuple (row,column)"""
        assert 0 <= value <= 9, "All numbers in the block must be between 1 and 9 (inclusive)."
        if value in self._values and value in self._block:
            raise ValueError("The value is already in block.")
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

    @property
    def board(self):
        return self._board

    @property
    def rowUnit(self):
        rows = []
        for i in range(0,9):
            row = []
            for j in range(0,9):
                row.append((i,j))
            rows.append(row)
        return rows

    @property
    def columnUnit(self):
        columns = []
        for i in range(0,9):
            column = []
            for j in range(0,9):
                column.append((j,i))
            columns.append(column)
        return columns

    @property
    def boxUnit(self):
        boxes = []
        for i in [[0,1,2],[3,4,5],[6,7,8]]:
            for j in [[0,1,2],[3,4,5],[6,7,8]]:
                box = [(a,b) for a in i for b in j]
                boxes.append(box)
        return boxes

    @property
    def unitlist(self):
        return (self.rowUnit+self.columnUnit+self.boxUnit)

    @property
    def units(self):
        units = dict()
        for square in self._points:
            for unit in self.unitlist:
                if square in unit:
                    units[square] = units.get(square,[])
                    units[square].append(unit)
        return units

    @property
    def peers(self):
        peers = dict()
        for point in self._points:
            point_peers = set()
            for unit in self.units[point]:
                for square in unit:
                    if square != point:
                        point_peers.add(square)
            peers[point] = point_peers
        return peers

    @property
    def _rows(self):
        rows = []
        for i in range(0, 9):
            row = []
            for j in range(0,9):
                row.append(self.board[i-(i%3)+j//3][(i%3,j%3)])
            rows.append(row)
        return rows

    @property
    def _columns(self):
        columns = []
        for i in range(0,9):
            column = []
            for j in range(0,9):
                column.append(self.board[j-(j%3)+i//3][(j%3,i%3)])
            columns.append(column)
        return columns

    @property
    def isSolved(self):
        for column in self._columns:
            if sum(column) != 45:
                return False
        for row in self._rows:
            if sum(row) != 45:
                return False
        for box in self._board:
            if sum(box.block) != 45:
                return False
        return True

    def __setitem__(self, point, value):
        assert 0 <= (point[0] and point[1]) <= 8, "The value must be inside the Sudoku board!"
        assert 0 <= value <= 9, "The value must be between 1 and 9 (inclusive)."
        block_point = (point[0]//3, point[1]//3)
        targetblock = self.board[3*block_point[0] + block_point[1]]
        targetblock[point[0]%3, point[1]%3] = value

    def __getitem__(self, point):
        block_point = (point[0]//3, point[1]//3)
        targetblock = self.board[3*block_point[0] + block_point[1]]
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
                result += str(self.board[i*3+j%3]).split('\n')[j//3]
        return result
