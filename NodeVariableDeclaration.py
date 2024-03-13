class NodeVariableDeclaration:
    def __init__(self, type_specification, variable_name, expression=None, array_size=None, variable_list=None):
        self.type_specification = type_specification
        self.variable_name = variable_name
        self.expression = expression
        self.array_size = array_size
        self.variable_list = variable_list
