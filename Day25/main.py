from scanner import Scanner
from terminal import TokenType


scanner = Scanner("input/test.txt")

token = scanner.get_token()
while token.type != TokenType.EOF:
    print(token.type)
    token = scanner.get_token()
