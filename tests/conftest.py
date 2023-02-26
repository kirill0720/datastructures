import pytest
from datastructures.binary_search_tree import BinarySearchTree


@pytest.fixture
def bst():
    """BST with root id == 40."""
    bst = BinarySearchTree()
    data = {'id': 40}
    bst.insert(data)
    return bst
