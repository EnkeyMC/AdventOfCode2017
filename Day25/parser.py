from grammar import NonTerminal, Grammar
from stack import Stack


class SAParser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.grammar = Grammar()

    def parse(self):
        dtree_stack = Stack()
        dtree_stack.push(self.grammar.start_nonterminal)

        while not dtree_stack.is_empty():
            token = self.scanner.get_token()

            while SAParser._is_nonterminal_on_top(dtree_stack):
                rule = self.grammar.get_rule(dtree_stack.peek(), token)
                for rule_part in rule:
                    dtree_stack.push(rule_part)

            if dtree_stack.peek() != token.type:
                raise SyntaxError("Unexpected terminal: ", repr(token))

    @staticmethod
    def _is_nonterminal_on_top(stack):
        return isinstance(stack.peek(), NonTerminal)
