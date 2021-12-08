#!/usr/bin/env python
import sys
import copy
from itertools import chain

test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def main():

    # read in the file as an array
    with open('../../data/05/input.txt') as fin:
        input = fin.read().splitlines()

    # input = test_data.splitlines()

    coords = []

    diagram = [ [0] * len(input)*2 for _ in range(len(input) * 2)]

    print(diagram)
    coords = []

    for line in input:

        a, b = line.partition(' -> ')[::2]
        a = make_int_tuple(a)
        b = make_int_tuple(b)
        if a[0] == b[0] or a[1] == b[1]:
            coords.append([a, b])

    for coord in coords:
        if coord[0][0] == coord[1][0]:
            diagram = update_vertical(coord, diagram)
        else:
            diagram = update_horizontal(coord, diagram)

    for row in diagram:
        print(row)

    overlaps = 0

    for x in chain.from_iterable(diagram):
        if x > 1:
            overlaps += 1
    
    print(f'Overlaps: {overlaps}')


def update_vertical(coord, diagram):
    col = coord[0][0]
    # print(f'column: {col}')
    row_start = min(coord[0][1], coord[1][1])
    row_end = max(coord[0][1], coord[1][1])
    while row_start <= row_end:
        diagram[row_start][col] += 1
        row_start += 1
    return diagram

def update_horizontal(coord, diagram):
    row = coord[0][1]
    col_start = min(coord[0][0], coord[1][0])
    col_end = max(coord[0][0], coord[1][0])
    while col_start <= col_end:
        diagram[row][col_start] += 1
        col_start += 1
    return diagram



def make_int_tuple(a):
    x, y = map(int, a.split(','))
    return (x,y)

if __name__ == '__main__':
    main()