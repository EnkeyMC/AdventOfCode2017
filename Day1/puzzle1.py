

def calculate_sum(numbers):
    result = 0
    last_digit = int(numbers[len(numbers) - 1])

    for n in numbers:
        n = int(n)

        if last_digit == n:
            result += last_digit

        last_digit = n

    return result


def get_numbers(filename):
    with open(filename) as file:
        numbers = file.read()

    return numbers.strip()


if __name__ == "__main__":
    print(calculate_sum(get_numbers("puzzle-input/input.txt")))
