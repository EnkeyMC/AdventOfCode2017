from puzzle1 import get_numbers


def calculate_sum(numbers):
    result = 0

    for i in range(0, len(numbers)):
        n = int(numbers[i])
        half_idx = int((i + (len(numbers) / 2)) % len(numbers))
        next_digit = int(numbers[half_idx])

        if next_digit == n:
            result += n

    return result


if __name__ == "__main__":
    print(calculate_sum(get_numbers("puzzle-input/input.txt")))



