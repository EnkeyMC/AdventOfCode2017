import csv


def parse(filename):
    data = list()
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')

        for row in reader:
            row = [int(x) for x in row]
            data.append(row)
    return data


def checksum(data):
    final_sum = 0

    for row in data:
        final_sum += max(row) - min(row)
    return final_sum


if __name__ == '__main__':
    print(checksum(parse("puzzle-input/input.txt")))
