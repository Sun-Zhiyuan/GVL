class NodeEqualityExpression:
    def __init__(self, left, operator=None, right=None):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        if self.operator:
            return f"EqualityExpression(left={self.left}, operator={self.operator}, right={self.right})"
        else:
            return f"EqualityExpression(expression={self.left})"
