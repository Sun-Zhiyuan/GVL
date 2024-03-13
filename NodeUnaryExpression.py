class NodeUnaryExpression:
    def __init__(self, operator=None, expression=None):
        self.operator = operator
        self.expression = expression

    def __str__(self):
        if self.operator:
            return f"UnaryExpression(operator={self.operator}, expression={self.expression})"
        else:
            return f"UnaryExpression(expression={self.expression})"