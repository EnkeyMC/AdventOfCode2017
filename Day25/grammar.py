from terminal import TokenType
from enum import Enum
from rule import Rule


class NonTerminal(Enum):
    PROGRAM = 1
    STATE = 2
    COMMAND_LIST = 3
    CMD_WRITE = 4
    CMD_MOVE = 5
    CMD_CONTINUE = 6
    DIR = 7


class Grammar:
    def __init__(self):
        self.start_nonterminal = NonTerminal.PROGRAM
        self.ll_table = {
            (NonTerminal.PROGRAM, TokenType.BEGIN): Rule([
                NonTerminal.STATE,
                TokenType.DOT,
                TokenType.STEPS,
                TokenType.NUMBER,
                TokenType.CHECKSUM,
                TokenType.DOT,
                TokenType.STATE_NAME,
                TokenType.BEGIN
            ]),
            (NonTerminal.STATE, TokenType.IN_STATE): Rule([
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
            ]),
            (NonTerminal.STATE, TokenType.EOF): Rule([
                TokenType.EOF
            ]),
            (NonTerminal.COMMAND_LIST, TokenType.DASH): Rule([
                NonTerminal.CMD_CONTINUE,
                NonTerminal.CMD_MOVE,
                NonTerminal.CMD_WRITE
            ]),
            (NonTerminal.CMD_WRITE, TokenType.DASH): Rule([
                TokenType.DOT,
                TokenType.NUMBER,
                TokenType.WRITE,
                TokenType.DASH
            ]),
            (NonTerminal.CMD_MOVE, TokenType.DASH): Rule([
                TokenType.DOT,
                NonTerminal.DIR,
                TokenType.MOVE,
                TokenType.DASH
            ]),
            (NonTerminal.CMD_CONTINUE, TokenType.DASH): Rule([
                TokenType.DOT,
                TokenType.STATE_NAME,
                TokenType.CONTINUE,
                TokenType.DASH
            ]),
            (NonTerminal.DIR, TokenType.LEFT): Rule([
                TokenType.LEFT
            ]),
            (NonTerminal.DIR, TokenType.RIGHT): Rule([
                TokenType.RIGHT
            ])
        }

    def get_rule(self, nonterminal, terminal):
        try:
            return self.ll_table[(nonterminal, terminal)]
        except KeyError:
            raise SyntaxError("Unexpected token: " + repr(terminal))
