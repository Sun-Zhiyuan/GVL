class NodeWhileStatement:
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def __str__(self):
        return f"While(condition={self.condition}, block={self.block})"