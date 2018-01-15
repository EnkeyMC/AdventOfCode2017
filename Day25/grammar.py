from terminal import TokenType
from enum import Enum, auto


class NonTerminal(Enum):
    PROGRAM = auto
    STATE = auto
    COMMAND_LIST = auto
    CMD_WRITE = auto
    CMD_MOVE = auto
    CMD_CONTINUE = auto
    DIR = auto


class Grammar:
    def __init__(self):
        self.start_nonterminal = NonTerminal.PROGRAM
        self.ll_table = {
            (NonTerminal.PROGRAM, TokenType.BEGIN): [
                NonTerminal.STATE,
                TokenType.DOT,
                TokenType.STEPS,
                TokenType.NUMBER,
                TokenType.CHECKSUM,
                TokenType.DOT,
                TokenType.STATE_NAME,
                TokenType.BEGIN
            ],
            (NonTerminal.STATE, TokenType.IN_STATE): [
                NonTerminal.STATE,
                NonTerminal.COMMAND_LIST,
                TokenType.COLON,
                TokenType.NUMBER,
                TokenType.IF,
                NonTerminal.COMMAND_LIST,
                TokenType.COLON,
                TokenType.NUMBER,
                TokenType.IF,
                TokenType.COLON,
                TokenType.STATE_NAME,
                TokenType.IN_STATE
            ],
            (NonTerminal.STATE, TokenType.EOF): [
                TokenType.EOF
            ],
            (NonTerminal.COMMAND_LIST, TokenType.DASH): [
                NonTerminal.CMD_CONTINUE,
                NonTerminal.CMD_MOVE,
                NonTerminal.CMD_WRITE
            ],
            (NonTerminal.CMD_WRITE, TokenType.DASH): [
                TokenType.DOT,
                TokenType.NUMBER,
                TokenType.WRITE,
                TokenType.DASH
            ],
            (NonTerminal.CMD_MOVE, TokenType.DASH): [
                TokenType.DOT,
                NonTerminal.DIR,
                TokenType.MOVE,
                TokenType.DASH
            ],
            (NonTerminal.CMD_CONTINUE, TokenType.DASH): [
                TokenType.DOT,
                TokenType.STATE_NAME,
                TokenType.CONTINUE,
                TokenType.DASH
            ],
            (NonTerminal.DIR, TokenType.LEFT): [
                TokenType.LEFT
            ],
            (NonTerminal.DIR, TokenType.RIGHT): [
                TokenType.RIGHT
            ]
        }

    def get_rule(self, nonterminal, terminal):
        try:
            return self.ll_table[(nonterminal, terminal)]
        except KeyError:
            raise SyntaxError("Unexpected token: " + repr(terminal))
