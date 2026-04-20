from pathlib import Path

from functools import reduce


MAX_CUBES_FOR_PART_1 = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def text_generator():
    file_path = Path(__file__).parent / 'input.txt'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                game, plays = line.strip().split(': ')
                game_id = int(game.split(' ')[1])
                individual_pulls = plays.replace(';', ',').split(', ')
                processed_pulls = []
                for pull in individual_pulls:
                    amount, color = pull.split(' ')
                    processed_pulls.append((int(amount), color))
                yield (game_id, processed_pulls)
    except FileNotFoundError:
        print(f"Error: Could not find file.txt at {file_path}")
        return
def aoc_23_2_task_part1():
    total_result = 0
    for game_id, pulls in text_generator():
        if all(amount <= MAX_CUBES_FOR_PART_1[color] for amount, color in pulls):
            total_result += game_id
    return total_result

def aoc_23_2_task_part2():
    total_result = 0
    for line in text_generator():
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        _, plays = line
        for amount, color in plays:
            if int(amount) > max_cubes[color]:
                max_cubes[color] = int(amount)
        total_result += reduce(lambda x, y: x * y, max_cubes.values())
    return total_result