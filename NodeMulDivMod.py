class NodeMulDivMod:
    def __init__(self, operator, left_operand, right_operand):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand

    def __str__(self):
        return f"NodeMulDivMod(operator={self.operator}, left_operand={self.left_operand}, right_operand={self.right_operand})"