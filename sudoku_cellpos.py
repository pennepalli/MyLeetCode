#!/usr/bin/python3

import sys

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

if __name__ == "__main__":
    pos = int(sys.argv[1])
    boxnum = pos // 10
    cellnum = pos % 10
    x,y  = get_coordinates(boxnum, cellnum)
    print(x,y)
