from pathlib import Path
from functools import reduce
import re

MAP_STR_TO_NUM = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
OPTIONS = list(MAP_STR_TO_NUM.keys()) + list(MAP_STR_TO_NUM.values())
REGEX = "|".join(OPTIONS)
PATTERN = fr'(?=({REGEX}))'

def text_generator():
    file_path = Path(__file__).parent / 'file.txt'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: Could not find file.txt at {file_path}")
        return

def scan_line(line):
    all_digits = re.findall(PATTERN, line)
    return (all_digits[0], all_digits[-1])

def get_digit(string):
    return string if string.isdigit() else MAP_STR_TO_NUM[string]

def calculate_line(line: str):
    numbers = scan_line(line)
    return int(reduce(lambda acc, curr: acc + get_digit(curr), numbers, ""))


def aoc_23_1_task():
    lines = text_generator()
    total_result = 0
    for line in lines:
        total_result += calculate_line(line)
    return total_result