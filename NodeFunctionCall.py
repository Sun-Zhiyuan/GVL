class NodeFunctionCall:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return f"NodeFunctionCall(name={self.name}, arguments={self.arguments})"