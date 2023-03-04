from typing import Any


class Node:
    """Class to store data."""

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Node | None = None


class LinkedList:
    """Class to represent LinkedList data structure."""

    def __init__(self) -> None:
        self.__head: Node | None = None

    @property
    def head(self):
        return self.__head

    def insert(self, data: Any) -> None:
        """Insert data at the end of the LinkedList."""
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
        else:
            current_node = self.__head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def search(self, data_to_search: Any) -> bool:
        """Search an element in a Linked List (Iterative and Recursive)"""
        node: Node = self.__head
        while node:
            if node.data == data_to_search:
                return True
            node = node.next_node
        return False

    def delete(self, data: Any) -> None:
        """Delete all nodes where node.data == data."""
        if self.__head is None:
            return

        if self.__head.data == data:
            self.__head = self.__head.next_node
            return

        node = self.__head
        while node.next_node:
            if node.next_node.data == data:
                node.next_node = node.next_node.next_node
            node = node.next_node

    def __len__(self) -> int:
        """Find Length of a Linked List (Iterative and Recursive)"""
        count = 0
        node: Node = self.__head
        while node:
            count += 1
            node = node.next_node
        return count

    def __str__(self) -> str:
        """Return a string with data in the LinkedList separated by one space."""
        text = ''
        node: Node = self.__head
        while node:
            text += f'{node.data} '
            node = node.next_node
        return text.strip()
