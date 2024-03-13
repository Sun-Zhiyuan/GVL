class NodeLessThanOrEqual:
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def __str__(self):
        return f"LessThanOrEqual(left_expression={self.left_expression}, right_expression={self.right_expression})"