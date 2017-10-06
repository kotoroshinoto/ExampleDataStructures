from lists.linked.double import DoublyLinkedList


class DEQueue:
    def __init__(self):
        self.list = DoublyLinkedList()
        self._num_items = 0  # type: int

    def __len__(self) -> int:
        return self._num_items

    def __str__(self):
        return str(self.list)

    def enqueue(self, data: 'any'):
        self.list.push_front(data)
        self._num_items += 1

    def dequeue(self) -> 'any':
        node = self.list.pop_back()
        if node:
            self._num_items -= 1
            return node.get_data()
        else:
            return None
        
    def rev_enqueue(self, data: 'any'):
        self.list.push_back(data)
        self._num_items += 1

    def rev_dequeue(self) -> 'any':
        node = self.list.pop_front()
        if node:
            self._num_items -= 1
            return node.get_data()
        else:
            return None
