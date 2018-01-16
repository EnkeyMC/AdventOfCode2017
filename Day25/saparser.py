from grammar import NonTerminal, Grammar
from stack import Stack
from sem_an import SemanticAnalyzer


class SAParser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.grammar = Grammar()
        self.dtree_stack = Stack()
        self.sem_an_stack = Stack()
        self.dtree_stack.push(self.grammar.start_nonterminal)

    def parse(self):
        while not self.dtree_stack.is_empty():
            token = self.scanner.get_token()
            self._derive_till_terminal(token)
            self._handle_token(token)

    def _derive_till_terminal(self, token):
        while SAParser._is_nonterminal_on_top(self.dtree_stack):
            rule = self.grammar.get_rule(self.dtree_stack.peek(), token.type)
            if rule.sem_action is not None:
                self.sem_an_stack.push(SemanticAnalyzer(rule.sem_action))
            self._derive_by_rule(rule)

    def _derive_by_rule(self, rule):
        self.dtree_stack.pop()
        for rule_part in rule.rule_sequence:
            self.dtree_stack.push(rule_part)

    def _handle_token(self, token):
        if self.dtree_stack.pop() != token.type:
            raise SyntaxError("Unexpected terminal: " + repr(token.type))
        else:
            self._finish_analyzers()
            self.sem_an_stack.peek().analyze(self, token)

    def _finish_analyzers(self):
        while self.sem_an_stack.peek().finished:
            finished_sem_an = self.sem_an_stack.pop()
            self.sem_an_stack.peek().analyze(self, finished_sem_an.value)

    @staticmethod
    def _is_nonterminal_on_top(stack):
        return isinstance(stack.peek(), NonTerminal)
