from terminal import TokenType, Token


class Scanner:
    def __init__(self, filename):
        self.file = open(filename, 'rb')

    def get_token(self):
        string = ""

        while True:
            c = self.file.read(1).decode()
            if c:
                if TokenType.is_special(c) and len(string.strip()) > 0:
                    string = string.strip()
                    self.file.seek(-1, 1)
                    if string.isdigit():
                        return Token(TokenType.NUMBER, int(string))
                    return Token(TokenType.STATE_NAME, string)
                elif c == ' ' and string.strip().isdigit():
                    return Token(TokenType.NUMBER, int(string.strip()))

                string += c
                token_type = TokenType.get_token_type(string.strip())
                if token_type is not None:
                    return Token(token_type)
            else:
                return Token(TokenType.EOF)
