import re

# Const values
directory = "input/input.txt"
colors_list = ["blue", "green", "red"]
max_cubes_by_colors = {"blue": 14, "green": 13, "red": 12}


# Parse the file to extract the following information:
# - Names of different games
# - Number of cubes by colors in each line
# - Different colors present in each line
def parse_file(dir):
    lines = open(dir).read().split('\n')

    pattern = '|'.join(map(re.escape, colors_list))

    game_nbrs = []
    colors_nbr = []
    colors = []

    for i in range(len(lines) - 1):
        colors_nbr.append([int(nbr) for nbr in re.findall(r'-?\d+', lines[i])])
        game_nbrs.append(colors_nbr[i].pop(0))
        colors.append(re.findall(pattern, lines[i]))

    return game_nbrs, colors_nbr, colors


# Return True if the given number of colors (colors_nbr) is below the maximum authorized
# Otherwise, return False
def is_game_possible(colors, colors_nbr, max_cubes_by_colors):
    for i in range(len(colors)):
        if max_cubes_by_colors[colors[i]] < colors_nbr[i]:
            return False

    return True


# Resolve the day02-part1 problem
def main():
    result = 0
    game_nbrs, colors_nbr, colors = parse_file(directory)

    for i in range(len(game_nbrs)):
        if is_game_possible(colors[i], colors_nbr[i], max_cubes_by_colors):
            result += game_nbrs[i]

    return result


print(main())
