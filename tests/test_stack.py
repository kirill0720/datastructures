from datastructures.stack import Node, Stack


def test_node_init():
    node = Node(123)
    assert node.data == 123
    assert node.next_node is None


def test_stack_empty():
    """Create an empty Stack. Test that its size is 0."""
    stack = Stack()
    assert stack.size == 0


def test_stack_size1():
    """Push an element onto the stack. Test that its size is now 1."""
    stack = Stack()
    stack.push(1)
    assert stack.size == 1


def test_stack_size2():
    """Push another element onto the stack. Test that its size is now 2."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.size == 2


def test_stack_pop1():
    """Pop an element from the stack. Test that it matches the 2nd pushed value.
    Check that the size of the stack is now 1."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    data = stack.pop()
    assert data == 2
    assert stack.size == 1


def test_stack_pop2():
    """Pop an element from the stack. Test that it matches the 1st pushed value.
    Check that the size of the stack is 0."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    data = stack.pop()
    assert data == 1
    assert stack.size == 0


def test_stack_pop_from_empty():
    """Attempt to pop an element from the empry stack. You should receive None."""
    stack = Stack()
    data = stack.pop()
    assert data is None
    assert stack.size == 0


def test_stack_top():
    stack = Stack()
    stack.push(1)
    assert stack.top == 1
