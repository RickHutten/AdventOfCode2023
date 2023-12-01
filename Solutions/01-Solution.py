from Data import day_one as data


def is_digit(character: str) -> bool:
    return character.isnumeric()


def solve_for_digits(input_str: str) -> int:
    result = 0
    for line in input_str.split("\n"):
        number_of_line = ""
        for c in line:
            if is_digit(c):
                number_of_line += c
                break
        for c in line[::-1]:
            if is_digit(c):
                number_of_line += c
                break
        result += int(number_of_line)
    return result


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def get_starting_number(line: str) -> int | None:
    if line[0].isnumeric():
        return int(line[0])
    for size in [3, 4, 5]:
        if line[0:size] in numbers:
            return numbers[line[0:size]]


def get_ending_number(line: str) -> int | None:
    if line[-1].isnumeric():
        return int(line[-1])
    for size in [3, 4, 5]:
        if line[len(line)-size:] in numbers:
            return numbers[line[len(line)-size:]]


def solve_for_digits_and_letters(input_str: str) -> int:
    result = 0
    for line in input_str.split("\n"):
        number_of_line = ""
        for i in range(len(line)):
            number = get_starting_number(line[i:])
            if number is not None:
                number_of_line += str(number)
                break
        for i in range(len(line)):
            number = get_ending_number(line[:len(line) - i])
            if number is not None:
                number_of_line += str(number)
                break
        result += int(number_of_line)
    return result


print(solve_for_digits(data.test[0]))
print(solve_for_digits_and_letters(data.test[1]))
print(solve_for_digits(data.data[0]))
print(solve_for_digits_and_letters(data.data[1]))
