from parser import SAParser
from scanner import Scanner


if __name__ == "__main__":
    scanner = Scanner("input/test.txt")

    parser = SAParser(scanner)
    parser.parse()
