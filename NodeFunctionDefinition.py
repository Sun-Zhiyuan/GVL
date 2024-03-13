class NodeFunctionDefinition:
    def __init__(self, type_spec, identifier, formal_params, block):
        self.type_spec = type_spec
        self.identifier = identifier
        self.formal_params = formal_params
        self.block = block