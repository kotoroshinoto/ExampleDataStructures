from typing import Optional


class SingleLinkNode:
    def __init__(self, data: 'any'):
        self._data = data  # type: any
        self._next = None  # type: SingleLinkNode

    def get_data(self) -> 'any':
        return self._data

    def set_next(self, node: 'Optional[SingleLinkNode]'=None):
        self._next = node

    def get_next(self) -> 'SingleLinkNode':
        return self._next

    def insert_after(self, node: 'Optional[SingleLinkNode]'):
        node.set_next(self._next)
        self.set_next(node)

    def extract_after(self) -> 'SingleLinkNode':
        node = self.get_next()
        if node:
            self.set_next(node.get_next())
            node.set_next(None)
        return node
