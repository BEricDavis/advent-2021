#!/usr/binenv python
import sys

TEST = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7 """

def main():
    # read in the file as an array
    with open('../../data/04/input.txt') as fin:
        input = fin.read().splitlines()

    # the list of numbers that will be drawn
    nums = [int(i) for i in input[0].split(',')]
    print(nums)
    test_input = TEST.splitlines()
    boards = build_boards_array(test_input)
    for board in boards:
        print(board)

    for number in nums:
        # for each number drawn, see if the number is on a board
        boards = update_boards()
        check_for_bingo(boards)


def check_for_bingo(boards):
    bingo = False
    return bingo

def update_boards(boards, number):
    for board in boards:
        pass
    return boards

def build_boards_array(input):
    boards = [] 
    board = []
    for row in input[2:]:
    #     if row =="/n":
    #         boards.append(board)
    #         board = []
    #         continue
    #     else:
    #         board.append(row.split())
    # boards.append(board)
    # return boards

        if row == '':
            boards.append(board)
            board = []

        else:
            board.append([int(i) for i in row.split()])
    boards.append(board)
    return boards



        
 





if __name__ == '__main__':
    main()