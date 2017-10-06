from typing import Optional


class DoubleLinkNode:
    def __init__(self, data: 'any'):
        self._data = data
        self._next = None  # type: Optional[DoubleLinkNode]
        self._prev = None  # type: Optional[DoubleLinkNode]

    def get_data(self):
        return self._data

    def set_next(self, node: 'Optional[DoubleLinkNode]'=None):
        self._next = node

    def get_next(self) -> 'Optional[DoubleLinkNode]':
        return self._next

    def set_prev(self, node: 'Optional[DoubleLinkNode]'=None):
        self._prev = node

    def get_prev(self) -> 'Optional[DoubleLinkNode]':
        return self._prev

    def insert_after(self, node: 'Optional[DoubleLinkNode]'):
        # 0 -> 2 inserting 1 after 0 to get 0 -> 1 -> 2 (and 0 <- 1 <- 2)
        # 1.prev = 0;
        # 1.next = 2;
        # 2.prev = 1;
        # 0.next = 1
        # 1 is node, 0 is self, 2 is self.next
        next = self.get_next()
        node.set_prev(self)
        node.set_next(next)
        if next:
            next.set_prev(node)
        self.set_next(node)

    def insert_before(self, node: 'Optional[DoubleLinkNode]'):
        # 0 <- 2 inserting 1 before 2: 0 <- 1 <- 2 (and 0 -> 1 -> 2)
        # 1.prev = 0;
        # 1.next = 2;
        # 2.prev = 1;
        # 0.next = 1
        # 1 is node, 0 is self.prev, 2 is self
        prev = self.get_prev()
        node.set_prev(prev)
        node.set_next(self)
        if prev:
            prev.set_next(node)
        self.set_prev(node)

    def extract_after(self) -> 'Optional[DoubleLinkNode]':
        # 0 -> 1 -> 2 want to get 0 -> 2 (and 0 <- 2)
        # 0.next = 2
        # 2.prev = 0
        # 1.next = None
        # 1.prev = None
        # 0 is self, 1 is self.next, 2 is self.next.next
        node = self.get_next()
        if node:
            self.set_next(node.get_next())  # 0.next = 2
            node_next = node.get_next()
            if node_next:
                node_next.set_prev(self)  # 2.prev = 0
            node.set_prev(None)
            node.set_next(None)
        return node

    def extract_before(self) -> 'Optional[DoubleLinkNode]':
        # 0 <- 1 <- 2 want to get 0 <- 2 (and 0 -> 2)
        # 0.next = 2
        # 2.prev = 0
        # 1.next = None
        # 1.prev = None
        # 0 is self.prev.prev, 1 is self.prev, 2 is self
        node = self.get_prev()
        if node:
            self.set_prev(node.get_prev())  # 2.prev = 0
            node_prev = node.get_prev()
            if node_prev:
                node_prev.set_next(self)  # 0.next = 2
            node.set_prev(None)
            node.set_next(None)
        return node
