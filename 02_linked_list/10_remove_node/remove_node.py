class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_node(head, target_val):
    pass

def list_to_values(head):
    pass

def test_remove_node():
    # Test 00
    a, b, c, d, e, f = [Node(val) for val in ["a", "b", "c", "d", "e", "f"]]
    a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
    assert list_to_values(remove_node(a, "c")) == ["a", "b", "d", "e", "f"], "Test 00 failed"

    # Test 01
    x, y, z = [Node(val) for val in ["x", "y", "z"]]
    x.next, y.next = y, z
    assert list_to_values(remove_node(x, "z")) == ["x", "y"], "Test 01 failed"

    # Test 02
    q, r, s = [Node(val) for val in ["q", "r", "s"]]
    q.next, r.next = r, s
    assert list_to_values(remove_node(q, "q")) == ["r", "s"], "Test 02 failed"

    # Test 03
    node1, node2, node3, node4 = [Node(val) for val in ["h", "i", "j", "i"]]
    node1.next, node2.next, node3.next = node2, node3, node4
    assert list_to_values(remove_node(node1, "i")) == ["h", "j", "i"], "Test 03 failed"

    # Test 04
    t = Node("t")
    assert remove_node(t, "t") is None, "Test 04 failed"

    print("All tests passed!")

test_remove_node()
