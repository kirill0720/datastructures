from datastructures.queue import Queue, Node


def test_node_init():
    node = Node(123)
    assert node.data == 123
    assert node.next_node is None


def test_queue_empty():
    """Create an empty Queue. Test that its size is 0."""
    queue = Queue()
    assert queue.size == 0


def test_queue_size1():
    """Push an element onto the queue. Test that its size is now 1."""
    queue = Queue()
    queue.push(1)
    assert queue.size == 1


def test_queue_size2():
    """Push another element onto the queue. Test that its size is now 2."""
    queue = Queue()
    queue.push(1)
    queue.push(2)
    assert queue.size == 2


def test_queue_pop1():
    """Pop an element from the queue. Test that it matches the 2nd pushed value.
    Check that the size of the queue is now 1."""
    queue = Queue()
    queue.push(1)
    queue.push(2)
    data = queue.pop()
    assert data == 1
    assert queue.size == 1


def test_queue_pop2():
    """Pop an element from the queue. Test that it matches the 1st pushed value.
    Check that the size of the queue is 0."""
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.pop()
    data = queue.pop()
    assert data == 2
    assert queue.size == 0


def test_queue_pop_from_empty():
    """Attempt to pop an element from the empry queue. You should receive None."""
    queue = Queue()
    data = queue.pop()
    assert data is None
    assert queue.size == 0
