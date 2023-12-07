from functools import cmp_to_key

# Const values
directory = "input/input.txt"
scores = {
    "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8,
    "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13
}
patterns = [
    [1, 1, 1, 1, 1],
    [2, 1, 1, 1],
    [2, 2, 1],
    [3, 1, 1],
    [3, 2],
    [4, 1],
    [5],
]


# Parse the file to create a list parired value ex:
# [[32T3K, 765], [T55J5, 684]]
def parse_file(dir):
    result = []
    lines = open(dir).read().split('\n')

    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
        result.append([])

        for j in range(len(lines[i])):
            result[i].append(lines[i][j])

    return result[:-1]


# Compare the two strings if the two patterns are the same
def compare_string(s1, s2):
    for i in range(len(s1)):
        if scores[s1[i]] > scores[s2[i]]:
            return 1
        if scores[s1[i]] < scores[s2[i]]:
            return -1

    return 0


# Get the score of the given pattern based on his position in "paterns"
def get_string_patern_score(pattern):
    for i in range(len(patterns)):
        if pattern == patterns[i]:
            return i


# Get the pattern specified in the "patterns" const variable that correspond to the given string
def get_string_pattern(string):
    result = []

    while len(string):
        current_card = string[0]
        number_of_cards = string.count(current_card)

        string = string.replace(string[0], '')
        result.append(number_of_cards)

    result.sort(reverse=True)

    return result


# Function passed to sort built-in function to compare the score of two element
def compare(list1, list2):
    item1 = list1[0]
    item2 = list2[0]

    score1 = get_string_patern_score(get_string_pattern(item1))
    score2 = get_string_patern_score(get_string_pattern(item2))

    if score1 > score2:
        return 1
    elif score1 < score2:
        return -1
    elif score1 == score2:
        return compare_string(item1, item2)


# Reolve the day07-part1 problem
def main():
    key_pair = parse_file(directory)

    key_pair.sort(key=cmp_to_key(compare))

    result = 0
    for i in range(len(key_pair)):
        result += int(key_pair[i][1]) * (i + 1)

    return result


print(main())
