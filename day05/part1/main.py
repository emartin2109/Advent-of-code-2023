import re

# Const values
directory = "input/input.txt"


# Parse the file to extract the following information:
# - A conversion table containing a list of the different conversion steps from seeds to location
# - The seeds that needs to be planted
def parse_file(dir):
    blocks = open(dir).read().split("\n\n")
    seeds = [int(nbr) for nbr in re.findall(r'-?\d+', blocks[0])]
    conversion_table = []

    for i in range(1, len(blocks)):
        conversion_table.append(blocks[i].split("\n"))
        for j in range(len(conversion_table[i - 1])):
            conversion_table[i - 1][j] = [int(nbr) for nbr in re.findall(r'-?\d+', conversion_table[i - 1][j])]
        conversion_table[i - 1].pop(0)
    conversion_table[-1].pop()

    return conversion_table, seeds


# Resolve the day05-part1 problem
def main():
    conversion_table, seeds = parse_file(directory)

    for block in conversion_table:
        for i in range(len(seeds)):
            for line in block:
                dest_start = line[0]
                source_start = line[1]
                range_len = line[2]

                if int(seeds[i]) >= source_start and int(seeds[i]) < source_start + range_len:
                    seeds[i] = int(seeds[i]) + dest_start - source_start
                    break

    return min(seeds)


print(main())
