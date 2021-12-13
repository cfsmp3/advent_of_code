#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict

        
test_case = [
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7",
]

"""
with open("input-3a.txt") as f:
    lines = f.read().splitlines()
"""
def build_board (data):
    print ("Building board")
    print (data)
    matrix = [[int(i) for i in line.split()] for line in data[1:]]
    board = {'numbers': {}, 'rows': [], 'columns': []}
    for row_idx,row in enumerate(matrix):
        board['rows'].append (set ([i for i in row]))
        for col_idx,number in enumerate(row):
            if row_idx == 0:
                board['columns'].append(set ())
            board['columns'][col_idx].add(number)
            board['numbers'][number] = {'row': row_idx, 'col': col_idx}

    return (board)

def parse_input (lines):
    numbers = [int(x) for x in lines[0].split(',')]
    boards = []
    pos = 1
    while pos < len(lines):
        boards.append (build_board (lines[pos:pos+6]))
        pos += 6
    return numbers, boards

def scratch_number (board, number):
    won = False
    if number not in board['numbers']:
        return
    number_pos = board['numbers'][number]
    # print (f"Number: {number}, Number_pos: {number_pos}")
    board['rows'][number_pos['row']].remove (number)
    if len (board['rows'][number_pos['row']]) == 0:
        won = True
    board['columns'][number_pos['col']].remove (number)
    if len(board['columns'][number_pos['col']]) == 0:
        won = True
    del(board['numbers'][number])
    return won

def board_score(board, number):
    return sum(board['numbers'].keys()) * number

"""
numbers, boards = parse_input(test_case)
print (numbers)
print (boards)
"""
with open("input-4a.txt") as f:
    lines = f.read().splitlines()

numbers, boards = parse_input(lines)

remaining = set(x for x in range(len(boards)))
for number in numbers:
    for board_num, board in enumerate (boards):
        if board_num not in remaining: # Already won
            continue
        if scratch_number(board, number):
            print (f"Board {board_num} won!")
            print (f"Score: {board_score(board, number)}")
            remaining.remove(board_num)
            if len(remaining) == 0:
                print ("We're done")
                sys.exit(0)


