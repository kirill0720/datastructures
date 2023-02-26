from typing import Any


class Node:
    """Class to store data."""

    def __init__(self, data: Any, next_node: 'Node' = None) -> None:
        self.data = data
        self.next_node = next_node


class Queue:
    """Class to represent Queue data structure. First In First Out."""

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None

    def push(self, data: Any) -> None:
        """Add data into Queue."""
        if self.__head is None:
            self.__head = self.__tail = Node(data)
        else:
            self.__tail.next_node = Node(data)
            self.__tail = self.__tail.next_node

    def pop(self) -> Any | None:
        """Remove first added data from the Queue and return removed data."""
        if self.__head is not None:
            data = self.__head.data
            self.__head = self.__head.next_node
            if self.__head is None:
                self.__tail = None
            return data

    @property
    def size(self) -> int:
        """Returns number of elements in the queue."""
        count = 0
        node = self.__head
        while node:
            count += 1
            node = node.next_node
        return count
