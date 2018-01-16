from enum import Enum
from terminal import TokenType


class SemanticException(Exception):
    pass


class SemState(Enum):
    INIT = 1


class SemanticAnalyzer:
    def __init__(self, sem_action):
        self.sem_action = sem_action
        self.state = SemState.INIT
        self.value = None
        self.finished = False

    def analyze(self, parser, value):
        self.sem_action(self, parser, value)


def sem_begin(sem_an, parser, value):
    if value == TokenType.STATE_NAME:
        pass

