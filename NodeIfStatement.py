class NodeIfStatement:
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def __str__(self):
        if self.else_block is not None:
            return f"IfElse(condition={self.condition}, if_block={self.if_block}, else_block={self.else_block})"
        else:
            return f"If(condition={self.condition}, if_block={self.if_block})"