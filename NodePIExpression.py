class NodePIExpression:
    def __init__(self, operator, expression):
        self.operator = operator  # 操作符，可以是 "++" 或 "--"
        self.expression = expression  # 要自增/自减的表达式

    def __str__(self):
        return f"NodePostIncrement(operator={self.operator}, expression={self.expression})"