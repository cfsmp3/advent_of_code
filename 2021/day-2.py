#!/usr/bin/env python3

import sys

horz = 0
depth = 0
aim = 0

with open("input-2a.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        tokens = line.split()
        action = tokens[0]
        value = int(tokens[1])
        if action == 'forward':
            horz += value
            depth += value*aim
        elif action == 'down':
            aim += value
        elif action == 'up':
            aim -= value
        else:
            print (f"I don't know what {action } means")
            sys.exit(1)

    print (horz)
    print (depth)    
    print (horz * depth)
