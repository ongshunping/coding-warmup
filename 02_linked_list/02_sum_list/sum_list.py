class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sum_list(head):
    pass

def test_sum_list():
    # Test 00
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    assert sum_list(a) == 19, "Test 00 failed"

    # Test 01
    x = Node(38)
    y = Node(4)
    x.next = y
    assert sum_list(x) == 42, "Test 01 failed"

    # Test 02
    z = Node(100)
    assert sum_list(z) == 100, "Test 02 failed"

    # Test 03
    assert sum_list(None) == 0, "Test 03 failed"

    print("All tests passed!")

test_sum_list()
