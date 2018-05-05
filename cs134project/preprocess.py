#!/usr/bin/env python3
# (c) 2018 Hyeongjin Kim
# a script to read in Sudoku data

def sudoku_db(filename='sudoku.txt'):
    file = open(filename, 'r')
    db = []
    result = []
    s = file.readlines()
    index = -1
    for row in s:
        if row.strip()[0] == "G":
            index += 1
            db.append([])
            continue
        db[index].extend(row.strip())
    for e in db:
        temp = dict()
        for row in range(0,9):
            for column in range(0,9):
                temp[(row,column)] = int(e[9*row+column])
        result.append(temp)
    return result
