#!/bin/env python3
from collections import deque
from functools import reduce

input_dev = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678"
]

input_prod = []
with open("input-9a.txt", "r") as f:
    input_prod = f.read().splitlines()


def input_to_array (input):
    return [[int(c) for c in line] for line in input]

def is_local_min (input, x, y):
    return input[y][x] < min([
        input[y-1][x] if y>0 else float('inf'),
        input[y+1][x] if y<len(input)-1 else float('inf'),
        input[y][x-1] if x>0 else float('inf'),
        input[y][x+1] if x<len(input[0])-1 else float('inf')
    ])

def get_total_risk_level(input):
    return sum(
        [1 + input[y][x] 
            for y in range(len(input)) 
            for x in range(len(input[0])) if is_local_min(input, x,y)])

def get_basin_size(input, x, y):
    dq = deque ([(x,y)])
    size = 0
    while len(dq):
        cell_x, cell_y = dq.popleft()
        if cell_y < 0 or cell_y >= len(input):
            continue
        if cell_x < 0 or cell_x >= len(input[0]):
            continue
        if input[cell_y][cell_x] == 9 or input[cell_y][cell_x] == -1:
            continue
        size += 1
        input[cell_y][cell_x] = -1
        dq.append((cell_x+1, cell_y))
        dq.append((cell_x-1, cell_y))
        dq.append((cell_x, cell_y+1))
        dq.append((cell_x, cell_y-1))
    return size

def find_basins(input):
    basins = []
    for y in range (len (input)):
        for x in range(len(input[0])):
            if input[y][x] == 9 or input[y][x] == -1:
                continue
            basins.append (get_basin_size(input, x, y))
    top3 = sorted(basins, reverse=True)[:3]
    print (top3)
    print (reduce((lambda x, y: x * y), top3))

        
input = input_to_array(input_prod)


print (find_basins(input))