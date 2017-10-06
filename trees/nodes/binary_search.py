from .binary import BinaryNode


# note: inheritance of attributes and methods
class BinarySearchNode(BinaryNode):
    def __init__(self, data: 'any', key: int):
        super().__init__(data=data)
        self.key = key
        self.height = 1