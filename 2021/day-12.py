#!/bin/env python3
import sys
from collections import deque, Counter
from colorama import init, Fore

input_dev_1=[
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]

input_dev_2 = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc"
]

input_dev_3 = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW"
]

input_prod = [
    "zi-end",
    "XR-start",
    "zk-zi",
    "TS-zk",
    "zw-vl",
    "zk-zw",
    "end-po",
    "ws-zw",
    "TS-ws",
    "po-TS",
    "po-YH",
    "po-xk",
    "zi-ws",
    "zk-end",
    "zi-XR",
    "XR-zk",
    "vl-TS",
    "start-zw",
    "vl-start",
    "XR-zw",
    "XR-vl",
    "XR-ws",
]

all_journeys = []

def init_cave():
    return {"nodes": [], "next": 0}

def build_graph_part_a(input):
    graph = {}
    for line in input:
        from_cave, to_cave = line.split("-")
        if from_cave not in graph:
            graph[from_cave] = init_cave()
        if to_cave not in graph:
            graph[to_cave] = init_cave()

        graph[from_cave]["nodes"].append (to_cave)
        graph[to_cave]["nodes"].append (from_cave)
    return graph

def build_graph_part_b(input):
    graph = {}
    for line in input:
        from_cave, to_cave = line.split("-")
        if from_cave not in graph:
            graph[from_cave] = init_cave()
        if to_cave not in graph:
            graph[to_cave] = init_cave()

        if to_cave != 'start': # This prevents going back to start
            graph[from_cave]["nodes"].append (to_cave)
        if from_cave != 'start': # This prevents going back to start
            graph[to_cave]["nodes"].append (from_cave)
    return graph


def journey_str(journey):
    res = ' -> '.join ([cave_name for cave_name in journey])
    return res

def print_journey(journey):
    print (journey_str(journey))

def visit (graph, cave_name = "start", journey = deque(), visits = Counter()):
    came_from = journey[-1] if len(journey) else None
    # print (f"Entry in cave: {cave_name}, I came from: {came_from} {journey_str(journey)}")
    journey.append(cave_name)
    if cave_name.islower():
        visits[cave_name] += 1
        # print (f"{Fore.YELLOW}Visits small cave {cave_name}: {visits[cave_name]}{Fore.WHITE}")
    if cave_name == "end": # Found the exit!
        print (f"{Fore.GREEN}>>> Found the exit! {len (all_journeys)} {Fore.WHITE}")
        all_journeys.append (journey_str(journey))
        print_journey(journey)
        if cave_name.islower():
            visits[cave_name] -= 1
        journey.pop()
        return 1
    exits_found = 0
    cave = graph[cave_name]

    # print (f"From here I can go to: {cave['nodes']}")
    for next_cave_name in cave['nodes']:
        #print (f"Considering {next_cave_name} which I'm visited already {visits[next_cave_name]}")
        if next_cave_name.islower(): # Check if we can do it
            if visits[next_cave_name] > 1: # Definitely not
                continue
            if len(visits) > 0:
                top = visits.most_common(1)[0][1]
                #print (f" V/T: {visits} {top}")
                #print (f"Have I visited a small cave twice already: {top > 1}  ??? {top}")
                if top > 1 and visits[next_cave_name] > 0: # This would be the second small one visited twice
                    continue
        
        #print (f"I can visit {next_cave_name}, let's go")
        #print (f"* Journey before: {journey}")
        exits_found += visit(graph, next_cave_name, journey)
        #print (f"* Journey After: {journey}")
        #print (f"Back to {cave_name}, exits so far: {exits_found}")
    #print ("I can't go anything else, exiting")
    if cave_name.islower():
        visits[cave_name] -= 1
    journey.pop()
    return exits_found

init()
graph = build_graph_part_b(input_prod)
print (graph)

visits = Counter()
print (visit (graph, "start", visits = visits))
print (all_journeys)
s = sorted(all_journeys)
for idx, j in enumerate(s):
    print (f"{idx} _> {j}")
print (len(all_journeys))
print (len(set (all_journeys)))
print (visits)