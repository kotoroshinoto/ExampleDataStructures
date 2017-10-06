from lists.linked.single import SinglyLinkedList


class Queue:
    def __init__(self):
        self.list = SinglyLinkedList()
        self._num_items = 0  # type: int

    def enqueue(self, data: 'any'):
        self.list.push_back(data)
        self._num_items += 1

    def dequeue(self) -> 'any':
        node = self.list.pop()
        if node:
            self._num_items -= 1
            return node.get_data()
        else:
            return None

    def __len__(self) -> int:
        return self._num_items

    def __str__(self):
        return str(self.list)
