#!/usr/bin/env python3

with open("input.txt") as f:
    lines = f.read().splitlines()
    inc = 0
    values = [int(line) for line in lines]
    prev = values[0] + values[1] + values[2]

    for i in range(3,len(values)):
        current = prev - values[i - 3] + values[i]
        print (f"{i}: Prev: {prev} :  Current: {current}")
        if current > prev:
            inc += 1
        prev = current
    
    print (inc)
