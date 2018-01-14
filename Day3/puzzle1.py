from math import sqrt, ceil, floor


def get_next_closest_odd_square(number):
    root = sqrt(number)
    root = ceil(root)
    if root % 2 == 0:
        root += 1
    return root


def get_distance_in_spiral(number):
    if number == 1:
        return 1

    size = get_next_closest_odd_square(number)
    center = floor(size / 2)
    max_number = size**2

    for n in range(max_number, max_number - 4*(size + 1), - size + 1):
        if n - size + 1 < number <= n:
            return center + abs(n - number - center)


if __name__ == '__main__':
    print(get_distance_in_spiral(361527))
