class SingleLinkNode:
    def __init__(self, data: 'any'):
        self.data = data  # type: any
        self.next = None  # type: SingleLinkNode


class DoubleLinkNode():
    def __init__(self, data: 'any'):
        self.data = data  # type: any
        self.next = None  # type: DoubleLinkNode
        self.prev = None  # type: DoubleLinkNode


class LinkedStack:
    def __init__(self):
        self._head = None  # type: SingleLinkNode
        self._num_items = 0

    def push(self, data: 'any'):
        node = SingleLinkNode(data)
        if self._head:
            node.next = self._head
        self._head = node
        self._num_items += 1

    def pop(self) -> 'any':
        if self._head:
            node = self._head
            self._head = self._head.next
            self._num_items -= 1
            return node.data
        else:
            return None

    def __str__(self):
        s = []
        ptr = self._head
        while ptr:
            s.append(str(ptr.data))
            ptr = ptr.next
        return "->".join(s)

    def __len__(self):
        return self._num_items


class LinkedQueue:
    def __init__(self):
        self._head = None  # type: DoubleLinkNode
        self._tail = None  # type: DoubleLinkNode
        self._num_items = 0

    def __len__(self):
        return self._num_items

    def __str__(self):
        fs = []
        rs = []
        ptr = self._head
        while ptr:
            fs.append(str(ptr.data))
            ptr = ptr.next
        ptr = self._tail
        while ptr:
            rs.append(str(ptr.data))
            ptr = ptr.prev
        if len(fs) == 0:
            fs.append("None")
        if len(rs) == 0:
            rs.append("None")
        return "".join(["forward: ", "->".join(fs), "; reverse: ", "->".join(rs)])

    def enqueue(self, data: 'any'):
        node = DoubleLinkNode(data)
        if self._head:
            node.next = self._head
            self._head.prev = node
            self._head = node
        else:
            self._head = node
            self._tail = node
        self._num_items += 1

    def dequeue(self) -> 'any':
        if self._tail:
            node = self._tail
            self._tail = self._tail.prev
            if self._tail:
                self._tail.next = None
            else:
                self._head = None
            self._num_items -= 1
            return node.data
        else:
            return None


class LinkedDoubleEndedQueue(LinkedQueue):
    def rev_enqueue(self, data: 'any'):
        node = DoubleLinkNode(data)
        if self._tail:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        else:
            self._tail = node
            self._head = node
        self._num_items += 1

    def rev_dequeue(self) -> 'any':
        if self._head:
            node = self._head
            self._head = self._head.next
            if self._head:
                self._head.prev = None
            else:
                self._tail = None
            self._num_items -= 1
            return node.data
        else:
            return None
