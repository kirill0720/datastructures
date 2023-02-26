import pytest
from datastructures.binary_search_tree import BinarySearchTree, Node


def test_node_init():
    """Node is initialized with data and None for left & right."""
    data = {'id': 40}
    node = Node(data)
    assert node.data == data
    assert node.left is None
    assert node.right is None


def test_bst_init():
    """BST root is empty when initialized."""
    bst = BinarySearchTree()
    assert bst.root is None


def test_bst_one_node(bst):
    """First node is the BST' root."""
    assert bst.root.data['id'] == 40


def test_bst_insert_left(bst):
    """Insert data to the left from root."""
    bst.insert({'id': 30})
    assert bst.root.data['id'] == 40
    assert bst.root.left.data['id'] == 30


def test_bst_insert_right(bst):
    """Insert data to the right from root."""
    bst.insert({'id': 50})
    assert bst.root.data['id'] == 40
    assert bst.root.right.data['id'] == 50


