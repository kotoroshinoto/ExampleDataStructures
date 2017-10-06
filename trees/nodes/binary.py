from .arbitrary import ArbitraryNode


# note: inheritance of attributes and methods
class BinaryNode(ArbitraryNode):
    def __init__(self, data: 'any'):
        super().__init__(data=data, numchildren=2)

    def left(self) -> 'BinaryNode':
        return self.get_child(0)

    def right(self) -> 'BinaryNode':
        return self.get_child(1)

    def set_left(self, node: 'BinaryNode'):
        self.set_child(0, node)

    def set_right(self, node: 'BinaryNode'):
        self.set_child(1, node)