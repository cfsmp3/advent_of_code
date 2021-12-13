#!/bin/env python3

from collections import Counter, deque
from statistics import median

input_dev = [
"[({(<(())[]>[[{[]{<()<>>",
"[(()[<>])]({[<{<<[]>>(",
"{([(<{}[<>[]}>{[]{[(<()>",
"(((({<>}<{<{<>}{[]{[]{}",
"[[<[([]))<([[{}[[()]]]",
"[{[{({}]{}}([{[{{{}}([]",
"{<[[]]>}<{[{[{[]{()[[[]",
"[<(<(<(<{}))><([]([]()",
"<{([([[(<>()){}]>(<<{{",
"<{([{{}}[<[[[<>{}]]]>[]]"
]

delimiters = { '(': ')',
               '[': ']',
               '{': '}',
               '<': '>'
            }

def get_first_illegal_char(line):
    stack = deque()
    for c in line:
        if c in delimiters:
            stack.append(c)
        else:
            op = stack.pop()
            if delimiters[op] != c:
                return c, None
    if len(stack) == 0:
        return None, None # All OK
    fix = ''
    while len(stack) > 0:
        fix=fix + (delimiters[stack.pop()])    
    return None, fix


input_prod = []
with open("input-10a.txt", "r") as f:
    input_prod = f.read().splitlines()

input = input_prod

score = {')': 3, ']': 57, '}': 1197, '>': 25137}
score_fix = {')': 1, ']': 2, '}': 3, '>': 4}

illegal_cnt = Counter()
total_incomplete = 0
all_scores = []

for line in input:
    c, missing = get_first_illegal_char(line)
    if c is not None:
        illegal_cnt[c] += 1

    total_incomplete = 0
    if missing is not None:    
        for m in missing:
            total_incomplete *= 5
            total_incomplete += score_fix[m]
        all_scores.append(total_incomplete)
    print (f'{line} | {c} | {missing} | {total_incomplete}')


total_corrupt = sum(illegal_cnt[key]*score[key] for key in illegal_cnt.keys())
all_scores = sorted(all_scores)
print (all_scores)
print (median (all_scores))

print (total_corrupt)