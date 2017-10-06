from lists.nodes.double import DoubleLinkNode


class DoublyLinkedList:
    def __init__(self):
        self._head = None  # type: DoubleLinkNode
        self._tail = None  # type: DoubleLinkNode

    def push_front(self, data: 'any'):
        node = DoubleLinkNode(data)
        if self._head:
            node.set_next(self._head)
            self._head.set_prev(node)
        else:
            self._tail = node
        self._head = node

    def push_back(self, data: 'any'):
        node = DoubleLinkNode(data)
        if self._tail:
            node.set_prev(self._tail)
            self._tail.set_next(node)
        else:
            self._head = node
        self._tail = node

    def pop_front(self) -> 'DoubleLinkNode':
        if self._head:
            node = self._head
            self._head = self._head.get_next()
            if self._head:
                self._head.set_prev(None)
            else:
                self._tail = None
            return node
        else:
            return self._head

    def pop_back(self) -> 'DoubleLinkNode':
        if self._tail:
            node = self._tail
            self._tail = self._tail.get_prev()
            if self._tail:
                self._tail.set_next(None)
            else:
                self._head = None
            return node
        else:
            return self._tail

    def __str__(self):
        fs = []
        rs = []
        ptr = self._head
        while ptr:
            fs.append(str(ptr.get_data()))
            ptr = ptr.get_next()
        ptr = self._tail
        while ptr:
            rs.append(str(ptr.get_data()))
            ptr = ptr.get_prev()
        if len(fs) == 0:
            fs.append("None")
        if len(rs) == 0:
            rs.append("None")
        return "".join(["forward: ", "->".join(fs), "; reverse: ", "->".join(rs)])
