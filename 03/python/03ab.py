#!/usr/bin/env python
from os import closerange
import sys

def main():
    # read in the file as an array
    with open('../../data/03/test.txt') as fin:
        input = fin.read().splitlines()

    # PART A
    print('Part A')
    ones = [0] * len(input[0])
    gamma_list = ones[:]
    epsilon_list = ones[:]
    for row in input:
        for idx, dig in enumerate(row):
            if int(dig) == 1:
                ones[idx] += 1
    # print(ones)
    for idx, val in enumerate(ones):
        if len(input) - val < val:
            gamma_list[idx] = 1
        if len(input) - val > val:
            epsilon_list[idx] = 1


    gamma = int(''.join(str(i) for i in gamma_list), 2)
    epsilon = int(''.join(str(i) for i in epsilon_list), 2)

    print(gamma, epsilon)

    print(f'power consumption: {gamma * epsilon}')


    # PART B
    print('\n###### Part B ######')


    o2_list = input[:]
    co2_list = input[:]

    finder(o2_list, gamma_list)

    # o2_number = o2_finder(o2_list, gamma_list)
    # print(f'o2_number: {o2_number} / {int(o2_number, 2)}')

    # co2_number = co2_finder(co2_list, epsilon_list)
    # print(f'co2_number: {co2_number} / {int(co2_number, 2)}')

    # print(f'life_support: {int(co2_number) * int(o2_number)}')

def finder



def finder(gas_list, mask_list, inc=1):
    index = -1
    print(f'mask_list: {mask_list}')
    for row in reversed(gas_list):
        print(f'remaining rows: {len(gas_list)}')
        print(f'evaluating {row}')
        for i, val in enumerate(row):
            print(i, val)
            if int(val) != int(mask_list[i]):
                print(f'{val} != {mask_list[i]}')
                print(f'deleting {gas_list[index]}')
                del gas_list[index]
                next
            else:
                print(f'{val} == {mask_list[i]}')
        index -= 1


def o2_finder(o2_list, gamma_list):
    while len(o2_list) >= 1:
        for o2_idx, row in enumerate(o2_list):
            for idx, val in enumerate(row):
                if int(row[idx]) != int(gamma_list[idx]):
                    del o2_list[o2_idx]
                    if len(o2_list) == 1:
                        return o2_list[0]


def co2_finder(co2_list, epsilon_list):
    while len(co2_list) >= 1:
        for co2_idx, row in enumerate(co2_list):
            for idx, val in enumerate(row):
                if int(row[idx]) != int(epsilon_list[idx]):
                    del co2_list[co2_idx]
                    if len(co2_list) == 1:
                        return co2_list[0]


if __name__ == '__main__':
    main()
