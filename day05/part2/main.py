import re

# Const values
directory = "input/input.txt"


# Parse the file to extract the following information:
# - A conversion table containing a list of the different conversion steps from seeds to location
# - The seeds that needs to be planted
def parse_file(dir):
    blocks = open(dir).read().split("\n\n")
    unparsed_seeds = [int(nbr) for nbr in re.findall(r'-?\d+', blocks[0])]
    seeds = []
    for i in range(0, len(unparsed_seeds), 2):
        seeds.append([int(unparsed_seeds[i]), int(unparsed_seeds[i + 1]) + int(unparsed_seeds[i])])
    conversion_table = []

    for i in range(1, len(blocks)):
        conversion_table.append(blocks[i].split("\n"))
        for j in range(len(conversion_table[i - 1])):
            conversion_table[i - 1][j] = [int(nbr) for nbr in re.findall(r'-?\d+', conversion_table[i - 1][j])]
        conversion_table[i - 1].pop(0)
    conversion_table[-1].pop()

    return conversion_table, seeds


# Resolve the day05-part2 problem
def main():
    conversion_table, seeds = parse_file(directory)
    for block in conversion_table:
        new_seeds = []
        while len(seeds):
            seed_start, seed_end = seeds.pop(0)
            seed_changed = False
            for line in block:
                dest_start, source_start, range_len = int(line[0]), int(line[1]), int(line[2])
                new_start = max(seed_start, source_start)
                new_end = min(seed_end, source_start + range_len)

                if new_end <= new_start:
                    continue

                new_seeds.append([new_start - source_start + dest_start, new_end - source_start + dest_start])

                if seed_end > new_end:
                    seeds.append([new_end, seed_end])
                if seed_start < new_start:
                    seeds.append([seed_start, new_start])

                seed_changed = True
                break

            if not seed_changed:
                new_seeds.append([seed_start, seed_end])

        seeds = new_seeds

    return min(seeds)[0]


print(main())
