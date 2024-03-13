class NodeFunctionNum:
    def __init__(self, graph, args):
        self.graph = graph
        self.args = args

    def __str__(self):
        return f"NodeFunctionNum({self.name}, {self.args})"