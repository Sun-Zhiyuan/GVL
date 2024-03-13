class NodeFormalParameter:
    def __init__(self, type_specification, parameter_id):
        self.type_specification = type_specification
        self.parameter_id = parameter_id


class NodeArrayParameter:
    def __init__(self, type_specification, parameter_id, array_size):
        self.type_specification = type_specification
        self.parameter_id = parameter_id
        self.array_size = array_size if array_size is not None else "unspecified"
