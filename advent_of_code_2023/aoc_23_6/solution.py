import numpy as np

input_data_part_1 = [(46, 208), (85, 1412), (75, 1257), (82,1410)]
input_data_part_2 = (46857582, 208141212571410)

def aoc_23_6_task_part1():
    ways_to_win = np.zeros(len(input_data_part_1), dtype=int)
    for index,(time, distance) in enumerate(input_data_part_1):
        all_times = np.arange(1,time)
        distances = (time - all_times) * all_times
        ways_to_win[index] = np.sum(distances > distance)
    return np.prod(ways_to_win)

def aoc_23_6_task_part2():
    time = input_data_part_2[0]
    distance = input_data_part_2[1]
    all_times = np.arange(1,time)
    distances = (time - all_times) * all_times
    return np.sum(distances > distance)
