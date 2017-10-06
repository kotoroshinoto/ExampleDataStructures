from lists.nodes.single import SingleLinkNode


class SinglyLinkedList:
    def __init__(self):
        self._head = None  # type: SingleLinkNode
        self._tail = None  # type: SingleLinkNode

    def push(self, data: 'any'):
        node = SingleLinkNode(data)
        if self._head:
            node.set_next(self._head)
        else:
            self._tail = node
        self._head = node

    def push_back(self, data: 'any'):
        node = SingleLinkNode(data)
        if self._tail:
            self._tail.set_next(node)
            self._tail = node
        else:
            self._head = node
            self._tail = node

    def pop(self) -> 'SingleLinkNode':
        node = self._head  # type: SingleLinkNode
        if node:
            if self._head is self._tail:
                self._head = None
                self._tail = None
            else:
                self._head = node.get_next()
        return node

    def __str__(self):
        s = []
        ptr = self._head
        while ptr:
            s.append(str(ptr.get_data()))
            ptr = ptr.get_next()
        return "->".join(s)
