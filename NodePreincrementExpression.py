class NodePreIncrementExpression:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"PreIncrementExpression(expression={self.expression})"