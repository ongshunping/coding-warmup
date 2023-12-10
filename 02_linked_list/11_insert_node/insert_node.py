class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, value, index):
    pass

def list_to_values(head):
    pass

def test_insert_node():
    # Test 00
    a, b, c, d = [Node(val) for val in ["a", "b", "c", "d"]]
    a.next, b.next, c.next = b, c, d
    assert list_to_values(insert_node(a, 'x', 2)) == ["a", "b", "x", "c", "d"], "Test 00 failed"

    # Test 01
    a, b, c, d = [Node(val) for val in ["a", "b", "c", "d"]]
    a.next, b.next, c.next = b, c, d
    assert list_to_values(insert_node(a, 'v', 3)) == ["a", "b", "c", "v", "d"], "Test 01 failed"

    # Test 02
    a, b, c, d = [Node(val) for val in ["a", "b", "c", "d"]]
    a.next, b.next, c.next = b, c, d
    assert list_to_values(insert_node(a, 'm', 4)) == ["a", "b", "c", "d", "m"], "Test 02 failed"

    # Test 03
    a, b = [Node(val) for val in ["a", "b"]]
    a.next = b
    assert list_to_values(insert_node(a, 'z', 0)) == ["z", "a", "b"], "Test 03 failed"

    print("All tests passed!")

test_insert_node()
