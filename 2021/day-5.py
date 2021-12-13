#!/usr/bin/env python3
import re
from collections import Counter

def load (data):
    prog = re.compile("((?:\d)+),((?:\d)+)\D* ((?:\d)+),((?:\d)+)")

    hits = Counter()

    for line in data:
        result = prog.match(line)
        x1 = int (result.group(1))
        y1 = int (result.group(2))
        x2 = int (result.group(3))
        y2 = int (result.group(4))

        print (f"\n{x1},{y1} => {x2},{y2}")
        
        if x1 != x2 and y1 != y2: # Diagonal
            x = x1
            y = y1
            distance = abs(x2 - x1) + 1
            step_x = 1 if x2 > x1 else -1
            step_y = 1 if y2 > y1 else -1

            for _ in range(distance):
                hits[(x,y)] += 1
                print (f"   {x,y}")
                y += step_y
                x += step_x
            continue


        if x1 == x2: # Vertical line from y1 to y2
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2+step, step):
                hits[(x1,y)] += 1
                print (f"   {x1,y}")
        else:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2+step, step):
                hits[(x,y1)] += 1
                print (f"   {x,y1}")

    print (hits)
    danger = [key for key in hits.keys() if hits[key] > 1]
    print (danger)
    return len(danger)

"""
test_case = [
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2",
]

print (load (test_case))
"""

with open("input-5a.txt") as f:
    lines = f.read().splitlines()
    print (load (lines))

