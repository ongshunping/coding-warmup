class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values(head):
    pass

def test_linked_list_values():
    # Test 00
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    assert linked_list_values(a) == ['a', 'b', 'c', 'd'], "Test 00 failed"

    # Test 01
    x = Node("x")
    y = Node("y")
    x.next = y
    assert linked_list_values(x) == ['x', 'y'], "Test 01 failed"

    # Test 02
    q = Node("q")
    assert linked_list_values(q) == ['q'], "Test 02 failed"

    # Test 03
    assert linked_list_values(None) == [], "Test 03 failed"

    print("All tests passed!")

test_linked_list_values()
