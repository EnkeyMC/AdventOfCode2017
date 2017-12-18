from puzzle1 import parse


def checksum(data):
    final_sum = 0

    for row in data:
        found = False
        for dividend in range(0, len(row)):
            for divisor in range(0, len(row)):
                if dividend != divisor:
                    if row[dividend] % row[divisor] == 0:
                        final_sum += row[dividend] / row[divisor]
                        found = True
                if found:
                    break
            if found:
                break

    return final_sum


if __name__ == '__main__':
    print(checksum(parse("puzzle-input/input.txt")))
