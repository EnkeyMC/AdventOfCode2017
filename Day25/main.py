from scanner import Scanner


if __name__ == "__main__":
    scanner = Scanner("input/test.txt")

    from parser import SAParser
    parser = SAParser(scanner)
    parser.parse()
