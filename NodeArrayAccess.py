class NodeArrayAccess:
    def __init__(self, array_id, index):
        self.array_id = array_id
        self.index = index

    def __str__(self):
        return f"NodeArrayAccess(array_id={self.array_id}, index={self.index})"