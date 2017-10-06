from .nodes.binary_search import BinarySearchNode
from .binary_search import BinarySearchTree


class BinarySearchTreeRecursiveAVL(BinarySearchTree):
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
