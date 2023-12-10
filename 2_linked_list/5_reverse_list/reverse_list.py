class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    pass

def list_to_values(head):
    pass

def test_reverse_list():
    # Test 00
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    reversed_head = reverse_list(a)
    assert list_to_values(reversed_head) == ["f", "e", "d", "c", "b", "a"], "Test 00 failed"

    # Test 01
    x = Node("x")
    y = Node("y")
    x.next = y
    reversed_head = reverse_list(x)
    assert list_to_values(reversed_head) == ["y", "x"], "Test 01 failed"

    # Test 02
    p = Node("p")
    reversed_head = reverse_list(p)
    assert list_to_values(reversed_head) == ["p"], "Test 02 failed"

    print("All tests passed!")

test_reverse_list()
