#!/usr/bin/python3

import sys

def get_box_and_cell(x, y):
    # Box number
    box_col = x // 3
    box_row = y // 3
    box_number = box_row * 3 + box_col + 1

    # Cell number within the 3x3 box
    cell_col = x % 3
    cell_row = y % 3
    cell_number = cell_row * 3 + cell_col + 1

    return box_number, cell_number

def get_coordinates(box_number, cell_number):
    box_row = (box_number - 1) // 3
    box_col = (box_number - 1) % 3
    box_start_x = box_col * 3
    box_start_y = box_row * 3

    cell_row = (cell_number - 1) // 3
    cell_col = (cell_number - 1) % 3
    print(box_row, box_col, box_start_x, box_start_y, cell_row,cell_number)

    x = box_start_x + cell_col
    y = box_start_y + cell_row
    return x, y  # Return (x, y)

def solve_sudoku(p):

    cell = {}
    boxvalues = {}
    cellvalidvalues = {}
    for i,r in enumerate(p):
        for j,c in enumerate(r):
            bn,cn = get_box_and_cell(j,i)
            print("Box_Cell:",bn,cn)
            key = bn * 10 + cn
            if c == '.':
                cell[key] = 0
                cellvalidvalues[key] = [1,2,3,4,5,6,7,8,9]
            else:
                v = int(c)
                cell[key] = v
                boxvalues[bn].append(v)

    for m,n in cell.items():
        
        boxnum = m//100
        row = (m//10) % 10
        col = m % 10
        print(m,n, row, col)
        if n == 0:
            for i in range(9):
                val = p[row][i]
                if val != 0 and val in cellvalidvalues[m]:
                    cellvalidvalues[m].remove(val)
                val = p[i][col]
                if val != 0 and val in cellvalidvalues[m]:
                    cellvalidvalues[m].remove(val)
                cellvalidvalues[m].remove(i)

    print(cell)

if __name__ == "__main__":
    puzzle1=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    solve_sudoku(puzzle1)
