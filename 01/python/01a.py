#!/usr/bin/env python

increase = 0
decrease = 0
previous = 0
# read in the file as an array
with open('../../data/01/inputa.txt') as fin:
    input = fin.read().splitlines()[1:]

for a in input:
    if int(a) > previous:
        increase += 1
    if int(a) < previous:
        decrease += 1
    previous = int(a)

print(f'Increased: {increase}')
print(f'Decreased: {decrease}')