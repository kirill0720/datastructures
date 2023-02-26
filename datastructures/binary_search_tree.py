class Node:
    """Store data of type dict in a Node. 'id' key is required in a dict."""

    def __init__(self, data) -> None:
        """Node's left and right refs are set by BST insert method."""
        self.data: dict = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    """Represents binary search tree (BST) data structure."""

    def __init__(self) -> None:
        """BST is always initialized as empty tree."""
        self.__root: Node | None = None

    @property
    def root(self):
        return self.__root

    def insert(self, data: dict) -> None:
        """Insert Node(data) to BST."""
        if self.__root is None:
            self.__root = Node(data)
        else:
            self._insert_recursive(data, self.__root)

    def _insert_recursive(self, data: dict, node: Node) -> None:
        """Define where to write Node(data): left or right from node."""

        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)

        if data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
