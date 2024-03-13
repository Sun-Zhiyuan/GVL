class NodeForStatement:
    def __init__(self, initialization, condition, post_increment, block):
        self.initialization = initialization
        self.condition = condition
        self.post_increment = post_increment
        self.block = block

    def __str__(self):
        return f"For(initialization={self.initialization}, condition={self.condition}, post_increment={self.post_increment}, block={self.block})"