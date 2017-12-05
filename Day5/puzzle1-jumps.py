from array import array


def parse(filename):
    arr = array('i')
    with open(filename) as file:

        for line in file:
            arr.append(int(line))
    return arr


def get_out_of_maze(maze):
    position = 0
    jumps = 0

    while 0 <= position < len(maze):
        old_idx = position
        position += maze[position]
        maze[old_idx] += 1
        jumps += 1

    return jumps


def main():
    maze = parse("puzzle1-input/input.txt")

    print(get_out_of_maze(maze))

    return 0

if __name__ == "__main__":
    main()
