from puzzle1_jumps import parse


def get_out_of_maze(maze):
    position = 0
    jumps = 0

    while 0 <= position < len(maze):
        old_idx = position
        position += maze[position]
        if maze[old_idx] >= 3:
            maze[old_idx] -= 1
        else:
            maze[old_idx] += 1

        jumps += 1

    return jumps


def main():
    maze = parse("puzzle-input/input.txt")

    print(get_out_of_maze(maze))

    return 0

if __name__ == "__main__":
    main()
