from datastructures.linkedlist import Node, LinkedList


def test_node():
    node = Node('data')
    assert node.data == 'data'
    assert node.next_node is None


def test_ll_insert(ll_123):
    assert ll_123.head.data == 1
    assert ll_123.head.next_node.data == 2
    assert ll_123.head.next_node.next_node.data == 3


def test_ll_delete_empty():
    ll = LinkedList()
    ll.delete(0)
    assert ll.head is None


def test_ll_delete_head():
    ll = LinkedList()
    ll.insert(1)
    ll.delete(1)
    assert ll.head is None


def test_ll_delete(ll_123):
    ll_123.delete(2)
    assert ll_123.head.data == 1
    assert ll_123.head.next_node.data == 3


def test_ll_search(ll_123):
    assert ll_123.search(1)
    assert ll_123.search(2)
    assert not ll_123.search(100)


def test_ll_len():
    """Insert data at the beginning and check it order."""
    ll = LinkedList()
    assert len(ll) == 0
    ll.insert(1)
    assert len(ll) == 1
    ll.insert(2)
    assert len(ll) == 2


def test_ll_str():
    """Test str dunder method returns in 'data1 data2' format."""
    ll = LinkedList()
    assert str(ll) == ''
    ll.insert('data')
    assert str(ll) == 'data'
    ll.insert(5)
    assert str(ll) == 'data 5'
    ll.insert([5])
    assert str(ll) == 'data 5 [5]'
