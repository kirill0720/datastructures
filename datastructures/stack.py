from typing import Any


class Node:
    """Class to store data and ref to next one."""

    def __init__(self, data: Any, next_node: 'Node' = None) -> None:
        self.data = data
        self.__next_node = next_node

    @property
    def next_node(self):
        return self.__next_node


class Stack:
    """Class to represent stack data structure. First In Last Out."""

    def __init__(self) -> None:
        """New stack is always empty."""
        self.__top: Node | None = None

    @property
    def top(self) -> Node:
        """Returns data of the stack' top element."""
        return self.__top.data

    def push(self, data: Any) -> None:
        """Add data into Stack."""
        if self.__top is None:
            self.__top = Node(data)
        else:
            self.__top = Node(data, self.__top)

    def pop(self) -> Any | None:
        """Remove last added data from the Stack and return removed data."""
        if self.__top is not None:
            data = self.__top.data
            self.__top = self.__top.next_node
            return data

    @property
    def size(self) -> int:
        """Returns number of elements in the stack."""
        count = 0
        node = self.__top
        while node:
            count += 1
            node = node.next_node
        return count
