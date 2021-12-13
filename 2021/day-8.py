#!/bin/env python3
from collections import defaultdict

input_dev = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
]

input_prod = []
with open("input-8a.txt", "r") as f:
    input_prod = f.read().splitlines()

def parse_input(input):
    res = []
    for line in input:
        segments, digits = line.split('|');
        segments = [''.join (sorted ([c for c in segment])) for segment in segments.strip().split (' ')]
        digits = [''.join (sorted ([c for c in digit])) for digit in digits.strip().split (' ')]
        res.append ((segments, digits))
    return res

input = parse_input (input_prod)
#print (input)

segments_to_digits = {2: [1], 3: [7], 
                      4: [4], 5: [2,3,5], 6: [0, 6, 9], 7:[8]}

unique = 0

real_segments = [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg","acf", "abcdefg", "abcdfg"
]

total_sum = 0

for entry_segments, entry_digits in input:
    # Enty contains segments, digits
    digit_candidates = [set() for _ in range(10)] # For each digit, any of these strings is a candidate
    for segment in entry_segments:
        for i in range(0,10):
            if len(segment) == len(real_segments[i]):
                digit_candidates[i].add(segment)

    print (digit_candidates)
    solutions = {}
    mapping = {}

    def is_compatible_with_solutions(segment, digit):
        print (f"Can {segment} be a solution for {digit}?")
        parts_segment = set (p for p in segment)
        for i in range(10):
            if i == digit or i not in solutions: # Already solved
                continue
            parts_sol = set ([p for p in solutions[i]])
            print (f"{i}, Segment: {parts_segment} , truth: {parts_sol}")
            diff_real = set([c for c in real_segments[digit]]) - set([c for c in real_segments[i]]) 
            diff_here = parts_segment - parts_sol
            print (f"Diffs: {diff_real} , {diff_here}")
            if len(diff_real) != len(diff_here):
                return False
        return True

    this_pass = 0
    while len(solutions) < 10: 
        # 
        for i in range(10):
            if len(digit_candidates[i]) == 1:
                sol_segment = list (digit_candidates[i])[0]
                solutions[i] = sol_segment
                mapping[sol_segment] = i
                for j in range(0,10):
                    if sol_segment in digit_candidates[i]:
                        digit_candidates[i].remove(sol_segment)

        for i in range(10):
            for digit_candidate in list(digit_candidates[i]):
                if not is_compatible_with_solutions(digit_candidate, i):
                    digit_candidates[i].remove(digit_candidate)

        print (f"Pass: {this_pass} , solutions = {solutions}")
        print (f"{digit_candidates}")
        this_pass += 1

    print ("Solved!") 
    print (mapping)
    final = ''.join ([str(mapping[digit]) for digit in entry_digits ])
    print (final)
    total_sum += int(final)

print (f"Type this: {total_sum}")