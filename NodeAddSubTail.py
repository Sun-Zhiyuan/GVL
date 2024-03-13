class NodeAddSubTail:
    def __init__(self, operator, expression, tail):
        self.operator = operator
        self.expression = expression
        self.tail = tail

    def __str__(self):
        return f"NodeAddSubTail({self.operator}, {self.expression}, {self.tail})"