from typing import Dict
from linked_list_structs import LinkedQueue, LinkedStack


class BinaryNode:
    def __init__(self, data: 'any'):
        self.data = data  # type: any
        self.left = None  # type BinaryNode
        self.right = None  # type BinaryNode


class ArbitraryNode:
    def __init__(self, data):
        self.data = data  # type: any
        self.children = dict()  # type: Dict[any, ArbitraryNode]


class BinarySearchNode(BinaryNode):
    def __init__(self, data: 'any', key: int):
        super().__init__(data=data)
        self.key = key


class BinarySearchTree:
    def __init__(self, avl_mode=False):
        self._head = None  # type: BinarySearchNode
        self._avl_mode = avl_mode

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
        if self._avl_mode:
            self._rebalance(node)

    def _rebalance(self, w):
        parents = LinkedStack()
        ptr = self._head
        while True:
            parents.push(ptr)
            
        pass
