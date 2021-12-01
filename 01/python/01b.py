#!/usr/bin/env python
import sys

increase = 0
decrease = 0

# read in the file as an array
with open('../../data/01/inputa.txt') as fin:
    input = fin.read().splitlines()

# convert all the entries to integers
input = [int(i) for i in input]

window_len = 3
start_index = 0
end_index = start_index + window_len

while end_index + 1 <= len(input):

    window_a = sum(input[start_index:end_index])
    window_b = sum(input[start_index+1:end_index+1])

    if window_a < window_b:
        increase += 1
    if window_a > window_b:
        decrease += 1

    start_index += 1
    end_index += 1

print(f'Increased: {increase}')
print(f'Decreased: {decrease}')