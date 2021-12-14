#!/bin/env python3
import sys

input_dev = [
"6,10",
"0,14",
"9,10",
"0,3",
"10,4",
"4,11",
"6,0",
"6,12",
"4,1",
"0,13",
"10,12",
"3,4",
"3,0",
"8,4",
"1,10",
"2,14",
"8,10",
"9,0",
"",
"fold along y=7",
"fold along x=5",
]

def load_input (input):
    sheet = set()
    folds = []
    for idx, line in enumerate(input):
        if not line:
            break
        dot = tuple ([int (i) for i in line.split(',')])
        sheet.add (dot)
    for line in input[idx+1:]:
        assert (line.startswith ("fold along"))
        folds.append(line[len("fold along")+1:])
    return sheet, folds

def fold_along_y(sheet, y):
    new_sheet = set()
    for dot in sheet:
        if dot[1] < y:
            new_sheet.add(dot)
        else:
            dist_to_fold = dot[1] - y
            new_y = y - dist_to_fold
            new_sheet.add((dot[0], new_y))
    return new_sheet

def fold_along_x(sheet, x):
    new_sheet = set()
    for dot in sheet:
        if dot[0] < x:
            new_sheet.add(dot)
        else:
            dist_to_fold = dot[0] - x
            new_x = x - dist_to_fold
            new_sheet.add((new_x, dot[1]))
    return new_sheet

input_prod = []
with open("input-13a.txt", "r") as f:
    input_prod = f.read().splitlines()

sheet, folds = load_input(input_prod)
for fold in folds:
    print (f"Before fold {fold}, dot count={len(sheet)}")
    if fold[0] == 'y':
        sheet = fold_along_y (sheet, int (fold[2:]))
    elif fold[0] == 'x':
        sheet = fold_along_x (sheet, int (fold[2:]))
    else:
        print ("This is broken")
        sys.exit(0)
    print (f"Before fold {fold}, dot count={len(sheet)}")

for y in range(1 + max([dot[1] for dot in sheet])):
    line = ""
    for x in range(1 + max([dot[0] for dot in sheet])):
        if (x,y) in sheet:
            line += "*"
        else:
            line += " "
    print (line)
