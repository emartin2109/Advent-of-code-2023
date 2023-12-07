# Const values
directory = "input/input.txt"


# Parse the file so it become a list of lines
def parse_file(dir):
    return open(dir).read().split("\n")[:-1]


# Set the calibration pair accordingly to the given number
def get_new_calibration_pair(first_calibration, last_calibration, number):
    if first_calibration is None:
        first_calibration = int(number)
        last_calibration = int(number)
    else:
        last_calibration = int(number)
    return first_calibration, last_calibration


# Get the calibration value hidden in the given line
def get_calibration_in_line(line):
    first_calibration = None
    last_calibration = None

    for i in range(len(line)):
        character = line[i]

        if character.isdigit():
            first_calibration, last_calibration = get_new_calibration_pair(first_calibration, last_calibration, character)

    return first_calibration * 10 + last_calibration


# Resolve the day01-part1 problem
def main():
    result = 0
    lines = parse_file(directory)

    for line in lines:
        result += get_calibration_in_line(line)

    return result


print(main())
