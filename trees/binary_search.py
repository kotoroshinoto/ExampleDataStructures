class BinarySearchTree:
    def __init__(self):
        self._head = None  # type: BinarySearchNode

    def insert(self, data, key):
        node = BinarySearchNode(data=data, key=key)
        if self._head:
            ptr = self._head
            while True:
                if node.key == ptr.key:
                    return
                elif node.key < ptr.key:
                    if not ptr.left:
                        ptr.left = node
                        break
                    else:
                        ptr = ptr.left
                else:  # node.key > ptr.key
                    if not ptr.right:
                        ptr.right = node
                        break
                    else:
                        ptr = ptr.right
        else:
            self._head = node

    def _rebalance(self, w):
        parents = LinkedStack()
        ptr = self._head
        while True:
            parents.push_front(ptr)
        pass
