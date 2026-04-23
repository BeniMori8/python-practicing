import math

from advent_of_code_2023.aoc_23_8.input import network, directions

def aoc_23_8_task_part1(current_location, suffix_of_target):
    steps = 0
    index_of_routes = 0
    while current_location[2] != suffix_of_target:
        if current_location[2] == suffix_of_target:
            break
        else:
            index_of_network = 0 if directions[index_of_routes] == 'L' else 1
            index_of_routes = (index_of_routes + 1) % len(directions)
            current_location = network[current_location][index_of_network]
            steps +=1
    return steps

def aoc_23_8_task_part2():
    all_routes_with_last_a = list(filter(lambda route: route[2] == 'A', network.keys()))
    list_of_all_routes = list(map(lambda route: aoc_23_8_task_part1(route, 'Z'), all_routes_with_last_a))
    return math.lcm(*list_of_all_routes)