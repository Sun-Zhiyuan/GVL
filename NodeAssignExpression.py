class NodeAssignExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"AssignExpression(left={self.left}, right={self.right})"