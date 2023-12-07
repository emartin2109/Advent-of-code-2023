import re
import math

# Const values
directory = "input/input.txt"


# Parse the file to create a list of lines
# Each line are represented by a list of the numbers they contain
def parse_file(dir):
    lines = open(dir).read().split('\n')
    for i in range(len(lines)):
        lines[i] = re.findall(r'\d+', lines[i])
    return lines


# Solve x in a quadratic equation for a given a, b and c
# Note that they are multiple solution to this equation but for simplicity we will only consider one
def solve_quadratic_equation(a, b, c):
    x = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    return x


# Resolve the day06-part1 problem
def main():
    result = 1
    input = parse_file(directory)
    time = []
    distance = []

    for i in range(len(input[0])):
        time.append(input[0][i])
        distance.append(input[1][i])

    for i in range(len(time)):
        best_score = int(time[i]) / 2
        ranging = best_score - solve_quadratic_equation(-1, int(time[i]), int(distance[i]) * -1)

        longest = math.floor((best_score + ranging) - 0.000001)
        shortest = math.ceil((best_score - ranging) + 0.000001)

        result *= (longest - shortest) + 1

    return result


print(main())
