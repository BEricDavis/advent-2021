#!/usr/bin/env python

hpos = 0
depth = 0

# read in the file as an array
with open('../../data/02/inputa.txt') as fin:
    input = fin.read().splitlines()

for instruction in input:
    direction, distance = instruction.split()

    if direction == 'forward':
        hpos += int(distance)
    if direction == 'up':
        depth -= int(distance)
    if direction == 'down':
        depth += int(distance)
print(f'HPOS: {hpos}')
print(f'DEPTH: {depth}')
print (f'Product: {hpos * depth}')