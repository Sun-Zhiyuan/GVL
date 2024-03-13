class NodeIfElseStatement:
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def __str__(self):
        return f"IfElse(condition={self.condition}, if_block={self.if_block}, else_block={self.else_block})"