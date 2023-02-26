import pytest
from datastructures.binary_search_tree import BinarySearchTree


@pytest.fixture
def bst():
    """BST with root id == 40."""
    bst = BinarySearchTree()
    data = {'id': 40}
    bst.insert(data)
    return bst


@pytest.fixture
def bst_full():
    """BST with 3 levels of nodes."""
    bst = BinarySearchTree()
    bst.insert({'id': 40})

    bst.insert({'id': 30})
    bst.insert({'id': 25})
    bst.insert({'id': 35})

    bst.insert({'id': 50})
    bst.insert({'id': 60})
    bst.insert({'id': 45})
    return bst
