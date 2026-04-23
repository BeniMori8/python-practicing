from pathlib import Path
import numpy as np


def text_generator():
    file_path = Path(__file__).parent / 'input.txt'
    try:
        with open(file_path, 'r') as file:
            index = 0
            for line in file:
                _, card_details = line.strip().split(': ')
                winning_numbers, all_numbers = card_details.split(' | ')
                yield (index, winning_numbers, all_numbers)
                index += 1
    except FileNotFoundError:
        print(f"Error: Could not find file.txt at {file_path}")
        return


def aoc_23_4_task_part1():
    total_result = 0
    for _, winning_numbers, all_numbers in text_generator():
        intersection_size = np.intersect1d(np.fromstring(winning_numbers, sep=' ', dtype=int) , np.fromstring(all_numbers, sep=' ', dtype=int)).size
        total_result += 2 ** (intersection_size - 1) if intersection_size > 0 else intersection_size
    return total_result


def aoc_23_4_task_part2():
    card_copies = np.ones(198, dtype=int)
    for index, winning_numbers, all_numbers in text_generator():
        count_of_cards = card_copies[index]
        intersection_size = np.intersect1d(np.fromstring(winning_numbers, sep=' ', dtype=int) , np.fromstring(all_numbers, sep=' ', dtype=int)).size
        if count_of_cards != 0:
            card_copies[index + 1: index + intersection_size + 1] += 1 * count_of_cards
    return card_copies.sum()