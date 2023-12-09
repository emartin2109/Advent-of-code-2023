import re

# Const values
directory = "input/input.txt"
colors_list = ["blue", "green", "red"]


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


# Get the fewest cube number for each possible colors
def get_fewest_cube_nbr(colors, colors_nbr):
    fewest_cube_nbr = {"blue": 0, "green": 0, "red": 0}

    for i in range(len(colors)):
        if (colors_nbr[i] > fewest_cube_nbr[colors[i]]):
            fewest_cube_nbr[colors[i]] = colors_nbr[i]

    return fewest_cube_nbr


# Resolve the day02-part2 problem
def main():
    result = 0
    game_nbrs, colors_nbr, colors = parse_file(directory)

    for i in range(len(game_nbrs)):
        set_cube_power = 1
        fewest_cube_nbr = get_fewest_cube_nbr(colors[i], colors_nbr[i])

        for color in fewest_cube_nbr.keys():
            set_cube_power *= fewest_cube_nbr[color]

        result += set_cube_power

    return result


print(main())
