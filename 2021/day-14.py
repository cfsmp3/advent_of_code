#!/bin/env python3
import sys
from collections import Counter
from math import ceil

input_dev = [
"NNCB",
"",
"CH -> B",
"HH -> N",
"CB -> H",
"NH -> C",
"HB -> C",
"HC -> B",
"HN -> C",
"NN -> C",
"BH -> H",
"NC -> B",
"NB -> B",
"BN -> B",
"BB -> N",
"BC -> B",
"CC -> N",
"CN -> C",
]

def load_input(input):
    template = input[0]
    rules = {}
    for rule in input[2:]:
        pair, new_elem = rule[:2], rule[6:]
        rules[pair] = new_elem
    return template, rules


input_prod = []
with open("input-14a.txt", "r") as f:
    input_prod = f.read().splitlines()

template, rules = load_input(input_prod)

pairs_cnt = Counter([template[i:i+2] for i in range(len(template)-1)])
for step in range(40):
    step_cnt = Counter()
    for pair in pairs_cnt:
        if pair in rules: # This pair converts into 2
            new_pair1 = pair[0] + rules[pair]
            new_pair2 =  rules[pair] + pair[1]
            step_cnt[new_pair1] += pairs_cnt[pair]
            step_cnt[new_pair2] += pairs_cnt[pair]
        else: # This pair remains unchanged
            step_cnt[pair] += pairs_cnt[pair]
    pairs_cnt = step_cnt

total = Counter()
for pair in pairs_cnt:
    total[pair[0]] += pairs_cnt[pair]
    total[pair[1]] += pairs_cnt[pair]

for c in total:
    total[c] = ceil(total[c]/2)

print(total.most_common(1)[0][1] - total.most_common()[-1][1])
