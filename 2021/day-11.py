#!/bin/env python3

from collections import deque
input_dev = [
"5483143223",
"2745854711",
"5264556173",
"6141336146",
"6357385478",
"4167524645",
"2176841721",
"6882881134",
"4846848554",
"5283751526",
]

input_mini = [
"11111",
"19991",
"19191",
"19991",
"11111"  
]

input_prod = [
"4836484555",
"4663841772",
"3512484556",
"1481547572",
"7741183422",
"8683222882",
"4215244233",
"1544712171",
"5725855786",
"1717382281"
]


def step(input):
    neighbours = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),(0,1),
                  (1,-1),(1,0),(1,1)]

    input = [[o+1 for o in line] for line in input]
    flashes_total = 0

    flash = deque()
    changes = True
    flashed = set()

    while changes:
        changes = False
        for y in range(len(input)):
            for x in range(len(input[0])):
                if input[y][x] > 9 and (y,x) not in flashed:
                    #print (f"Exploding {y},{x}")
                    flash.append((y,x))
                    flashed.add((y,x))
    
        while len(flash):
            octopus_y, octopus_x = flash.popleft()
            #print (f"Explosion of {octopus_y,octopus_x}")
            for n in neighbours:
                if 0 <= octopus_y+n[0] < len(input) and \
                    0 <= octopus_x+n[1] < len(input[0]):
                    #print (f"    Increasing {octopus_y+n[0]},{octopus_x+n[1]}")
                    input [octopus_y+n[0]][octopus_x+n[1]] += 1
                    changes = True


    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] > 9:
                input[y][x] = 0
                flashes_total += 1
    
    return input, flashes_total

def print_status(input, step):
    print (f"Step: {step}")
    for y in range(len(input)):
        print(input[y])
    print ()

def input_to_array (input):
    return [[int(c) for c in line] for line in input]

input = input_to_array (input_prod)
flashes_total = 0

print_status (input, 0)
first_all_flash = None

s = 0
while not first_all_flash:
    s += 1
    input, flashes = step(input)
    if flashes == len(input) * len(input[0]):
        first_all_flash = s
    print_status (input, s)
    flashes_total += flashes

print (flashes_total)
print (first_all_flash)