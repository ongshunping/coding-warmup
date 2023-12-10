class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_node_value(head, index):
    pass

def test_get_node_value():
    # Test 00
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    assert get_node_value(a, 2) == 'c', "Test 00 failed"

    # Test 01
    assert get_node_value(a, 3) == 'd', "Test 01 failed"

    # Test 02
    assert get_node_value(a, 7) is None, "Test 02 failed"

    # Test 03
    node1 = Node("banana")
    node2 = Node("mango")
    node1.next = node2
    assert get_node_value(node1, 0) == 'banana', "Test 03 failed"

    # Test 04
    assert get_node_value(node1, 1) == 'mango', "Test 04 failed"

    print("All tests passed!")

# Call the test function
test_get_node_value()
