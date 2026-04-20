from pathlib import Path
import re

ROW_LENGTH = 140
WINDOW_SIZE = 3
PADDED_ROW = ["." * ROW_LENGTH]

def text_generator_task1():
    file_path = Path(__file__).parent / 'input.txt'
    try:
        with open(file_path, 'r') as file:
            window = PADDED_ROW
            for index,line in enumerate(file):
                window.append(line.strip())
                if len(window) == WINDOW_SIZE:
                    yield window
                    window = window[1:]
            yield window + PADDED_ROW

    except FileNotFoundError:
        print(f"Error: Could not find file.txt at {file_path}")
        return

def text_generator_task2():
    file_path = Path(__file__).parent / 'input.txt'
    try:
        with open(file_path, 'r') as file:
            window = PADDED_ROW
            index_for_gen = 0
            for index,line in enumerate(file):
                window.append(line.strip())
                if len(window) == WINDOW_SIZE:
                    yield (index_for_gen, window)
                    window = window[1:]
                    index_for_gen+= 1
            yield (index_for_gen, window + PADDED_ROW)

    except FileNotFoundError:
        print(f"Error: Could not find file.txt at {file_path}")
        return

def is_symbol_exists(mini_block):
    print(mini_block)
    mini_block_as_string = "".join(mini_block)
    return re.search(r'[^0-9.]', mini_block_as_string)


def build_mini_block(block , start, end):
    x_start = 0 if start == 0 else start -1
    x_end = end+ 1 if end != ROW_LENGTH - 1 else ROW_LENGTH
    y_start = 0
    y_end =  len(block)
    return [row[x_start:x_end] for row in block[y_start:y_end]]

def aoc_23_3_task1():
    total_result = 0
    for block in text_generator_task1():
        line = block[1]
        for match in re.finditer(r'\d+', line):
            number = int(match.group())
            start = match.start()
            end = match.end()
            mini_block = build_mini_block(block, start, end)
            if is_symbol_exists(mini_block):
                total_result += number
    return total_result



def get_star_coords(mini_block, start, end, global_index):
    for block_index,row in enumerate(mini_block):
        for row_index,char in enumerate(row):
            if char == '*':
                star_x = global_index - 1 + block_index
                star_y = start + row_index
                return (star_x, star_y)
    return None


def aoc_23_3_task2():
    total_result = 0
    dict_of_stars ={}
    for index, block in text_generator_task2():
        line = block[1]
        for match in re.finditer(r'\d+', line):
            number = int(match.group())
            start = match.start()
            end = match.end()
            mini_block = build_mini_block(block, start, end)
            mini_block_start = max(match.start()-1, 0)
            mini_block_end = min(ROW_LENGTH, match.end() + 1)
            star_coords = get_star_coords(mini_block, mini_block_start, mini_block_end, index)
            if star_coords:
                if star_coords not in dict_of_stars:
                    dict_of_stars[star_coords] = []
                dict_of_stars[star_coords].append(number)
    for numbers in dict_of_stars.values():
        if len(numbers) == 2:
            total_result += (numbers[0] * numbers[1])
    return total_result
