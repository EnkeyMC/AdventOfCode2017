from enum import Enum


class TokenType(Enum):
    BEGIN = "Begin in state"
    CHECKSUM = "Perform a diagnostic checksum after"
    STEPS = "steps"
    DOT = "."
    IN_STATE = "In state"
    COLON = ":"
    IF = "If the current value is"
    DASH = "-"
    WRITE = "Write the value"
    MOVE = "Move one slot to the"
    RIGHT = "right"
    LEFT = "left"
    CONTINUE = "Continue with state"
    NUMBER = 99998
    STATE_NAME = 99999
    EOF = 100000

    @staticmethod
    def get_token_type(string):
        for token_type in TokenType:
            if token_type not in [TokenType.STATE_NAME, TokenType.EOF, TokenType.NUMBER]:
                if string == token_type.value:
                    return token_type
        return None

    @staticmethod
    def is_special(char):
        return char in ['.', '\n', ':', '-']


class Token:
    def __init__(self, token_type, data=None):
        self.type = token_type
        self.data = data
