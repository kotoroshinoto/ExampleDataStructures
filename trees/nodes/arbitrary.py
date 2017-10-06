from numpy import ndarray
from typing import Dict, Tuple, Iterable


class ArbitraryNode:
    def __init__(self, data: 'any', numchildren: int):
        self._data = data  # type: any
        self._links = ndarray([numchildren], dtype=ArbitraryNode)  # type: ndarray(Iterable(int), dtype=ArbitraryNode)

    def __call__(self, *args, **kwargs):
        return self._data

    def set_child(self, index: int, node: 'ArbitraryNode') -> bool:
        if index >= self._links.shape[0] or index < 0:
            return False
        else:
            self._links[index] = node
            return True

    def get_child(self, index: int) -> 'ArbitraryNode':
        if index >= self._links.shape[0] or index < 0:
            raise ValueError("Invalid index: ", index)
        else:
            return self._links[index]