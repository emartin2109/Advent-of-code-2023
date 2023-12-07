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


# Retrieve the current score of the scratch card, ignoring the multiplier
def get_score(winning_numbers, card_numbers):
    score = 0

    for number in card_numbers:
        if number in winning_numbers:
            score += 1

    return score


# Update the list of prizes that have been won
def update_prizes_list(score, game_nbr, prizes_list):
    for i in range(score):
        prizes_list.append(game_nbr + i + 1)

    return prizes_list


# Obtain the score multiplier based on the list of prizes
def get_score_multiplicator(game_nbr, prizes_list):
    multiplicator = 1

    for number in prizes_list:
        if number == game_nbr:
            multiplicator += 1

    return multiplicator


# Get the prizes that the current line/card has won
def get_line_prizes(line, prizes_list):
    card_numbers, winning_numbers = get_line_numbers(line)
    winning_numbers = parse_numbers_list(winning_numbers)
    card_numbers = parse_numbers_list(card_numbers)
    game_nbr = card_numbers.pop(0)

    score_multiplicator = get_score_multiplicator(game_nbr, prizes_list)
    score = get_score(winning_numbers, card_numbers)

    for i in range(score_multiplicator):
        prizes_list = update_prizes_list(score, game_nbr, prizes_list)

    return prizes_list


# Resolve the day04-part2 problem
def main():
    prizes_list = []
    lines = parse_file(directory)

    for line in lines:
        prizes_list = get_line_prizes(line, prizes_list)

    return len(prizes_list) + len(lines)


print(main())
