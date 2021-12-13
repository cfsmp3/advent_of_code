#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict

horz = 0
depth = 0
aim = 0

def part1():
    with open("input-3a.txt") as f:
        lines = f.read().splitlines()
        cnt = defaultdict(Counter)
        for line in lines:
            for idx, val in enumerate(line):
                cnt[idx][val] += 1

        gamma = ""
        epsilon = ""
        for idx in range (len(cnt.keys())):
            gamma += cnt[idx].most_common(1)[0][0]
            epsilon += cnt[idx].most_common(2)[1][0]

        print (gamma)
        print (epsilon)
        gamma = int(gamma,2)
        epsilon = int(epsilon, 2)
        print (gamma*epsilon)

def part2(lines):
    oxygen = -1
    input = lines
    width = len(input[0])
    for idx in range(width):
        print (f"{idx} : {input}")
        cnt = Counter([number[idx] for number in input])
        print (cnt)
        bit_criteria = '1' if cnt['1'] >= cnt['0'] else '0'
        print (bit_criteria)
        input = [line for line in input if line[idx] == bit_criteria]
        print (input)
        if len(input) == 1:
            print (f"End at {input}")
            oxygen = int(input[0], 2)
            break
        print()

    input = lines
    for idx in range(width):
        print (f"{idx} : {input}")
        cnt = Counter([number[idx] for number in input])
        print (cnt)
        bit_criteria = '0' if cnt['0'] <= cnt['1'] else '1'
        print (bit_criteria)
        input = [line for line in input if line[idx] == bit_criteria]
        print (input)
        if len(input) == 1:
            print (f"End at {input}")
            scrubber = int(input[0], 2)
            break
        print()


    print (f"Oxygen: {oxygen} - Scrubber: {scrubber}")
    print (oxygen * scrubber)
        
test_case = [
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"
]

with open("input-3a.txt") as f:
    lines = f.read().splitlines()

part2(lines)
