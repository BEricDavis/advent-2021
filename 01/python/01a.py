#!/usr/bin/env python

increase = 0
decrease = 0
previous = 0
with open('../../data/01/inputa.txt') as fin:
    input = fin.read().splitlines()[1:]

for a in input:
    print(a)
    if int(a) > previous:
        increase += 1
        print('increased')
    if int(a) < previous:
        decrease += 1
    previous = int(a)

print(f'Increased: {increase}')
print(f'Decreased: {decrease}')