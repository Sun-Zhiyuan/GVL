class NodePostDecrementExpression:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"PostDecrementExpression(expression={self.expression})"