class NodeReturnStatement:
    def __init__(self, expression_statement):
        self.expression_statement = expression_statement

    def __str__(self):
        return f"ReturnStatement({self.expression_statement})"