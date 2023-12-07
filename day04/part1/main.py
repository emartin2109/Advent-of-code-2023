import re

# Const values
directory = "input/input.txt"


# Parse the file to create a list of lines
def parse_file(dir):
    return open(dir).read().split("\n")[:-1]


# Extract all numbers present in each line, dividing them into card_numbers and winning_numbers
def get_line_numbers(line):
    line_parts = line.split('|')
    card_numbers = re.findall(r'\d+', line_parts[0])
    winning_numbers = re.findall(r'\d+', line_parts[1])
    return card_numbers, winning_numbers


# Convert the list of numbers from strings to integers
def parse_numbers_list(numbers_list):
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])

    return numbers_list


# Retrieve the current score of the scratch card
def get_score(winning_numbers, card_numbers):
    score = 0

    for number in card_numbers:
        if number in winning_numbers:
            if not score:
                score = 1
            else:
                score *= 2

    return score


# Get score of the given line
def get_line_score(line):
    card_numbers, winning_numbers = get_line_numbers(line)
    winning_numbers = parse_numbers_list(winning_numbers)
    card_numbers = parse_numbers_list(card_numbers)
    card_numbers.pop(0)

    score = get_score(winning_numbers, card_numbers)

    return score


# Resolve the day04-part1 problem
def main():
    result = 0
    lines = parse_file(directory)

    for line in lines:
        result += get_line_score(line)

    return result


print(main())
