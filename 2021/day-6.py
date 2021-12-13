#!/bin/env python3 

input_prod = "4,1,1,4,1,2,1,4,1,3,4,4,1,5,5,1,3,1,1,1,4,4,3,1,5,3,1,2,5,1,1,5,1,1,4,1,1,1,1,2,1,5,3,4,4,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,4,1,2,3,5,1,2,2,4,1,4,4,4,1,2,5,1,2,1,1,1,1,1,1,4,1,1,4,3,4,2,1,3,1,1,1,3,5,5,4,3,4,1,5,1,1,1,2,2,1,3,1,2,4,1,1,3,3,1,3,3,1,1,3,1,5,1,1,3,1,1,1,5,4,1,1,1,1,4,1,1,3,5,4,3,1,1,5,4,1,1,2,5,4,2,1,4,1,1,1,1,3,1,1,1,1,4,1,1,1,1,2,4,1,1,1,1,3,1,1,5,1,1,1,1,1,1,4,2,1,3,1,1,1,2,4,2,3,1,4,1,2,1,4,2,1,4,4,1,5,1,1,4,4,1,2,2,1,1,1,1,1,1,1,1,1,1,1,4,5,4,1,3,1,3,1,1,1,5,3,5,5,2,2,1,4,1,4,2,1,4,1,2,1,1,2,1,1,5,4,2,1,1,1,2,4,1,1,1,1,2,1,1,5,1,1,2,2,5,1,1,1,1,1,2,4,2,3,1,2,1,5,4,5,1,4"

input_dev = "3,4,3,1,2"



def family_from_one_fish_naive (status, days):
    day = 0
    fish = [status]
    print (f"{day}: {fish}")
    while day < days:
        next_fish = []
        to_append = 0
        for f in fish:
            if f == 0:
                next_fish.append(6)
                to_append += 1
            else:
                next_fish.append(f-1)
        next_fish  += [8 for _ in range(to_append)]
        fish = next_fish
        day += 1
        print (f"{day}: {fish}")
    return len(fish)

def families (statuses, days):
    # Empty table
    days_states = [ [0 for _ in range(9)] for _ in range(days+1)]
    # Initialize counters at day 0
    for status in statuses:
        days_states[0][status] += 1
    
    current_day = 1
    while current_day <= days:
        spawn = days_states[current_day-1][0] 
        for i in range (8):
            days_states[current_day][i] = days_states[current_day -1][i+1]
        days_states[current_day][8] = spawn
        days_states[current_day][6] += spawn
        print (f"{current_day}: {sum(days_states[current_day])}")
        current_day += 1

    # print (days_states)
    return (sum(days_states[current_day-1]))

fish = [int(x) for x in input_prod.split(',')]
#fish = [3]
days_to_run = 18
#print (f"Fish={fish}, days_to_run = {days_to_run}, naive = {sum (family_from_one_fish_naive(x, days_to_run) for x in fish)}")

print (families (fish, 256))
