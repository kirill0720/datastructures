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


def test_bst_insert_left_left(bst):
    """Insert data two times to require recursion."""
    bst.insert({'id': 30})
    bst.insert({'id': 25})
    assert bst.root.data['id'] == 40
    assert bst.root.left.data['id'] == 30
    assert bst.root.left.left.data['id'] == 25


def test_bst_insert_right_right(bst):
    """Insert data two times to require recursion."""
    bst.insert({'id': 50})
    bst.insert({'id': 60})
    assert bst.root.data['id'] == 40
    assert bst.root.right.data['id'] == 50
    assert bst.root.right.right.data['id'] == 60


def test_bst_get_data_for_empty_bst():
    bst = BinarySearchTree()
    assert bst.get_data_by_id(40) == {}


@pytest.mark.parametrize('data_id, data', [(40, {'id': 40}),
                                           (30, {'id': 30}),
                                           (25, {'id': 25}),
                                           (35, {'id': 35}),
                                           (50, {'id': 50}),
                                           (60, {'id': 60}),
                                           (45, {'id': 45}),
                                           (999, {}),
                                           ])
def test_bst_get_data_by_id(bst_full, data_id, data):
    assert bst_full.get_data_by_id(data_id) == data
