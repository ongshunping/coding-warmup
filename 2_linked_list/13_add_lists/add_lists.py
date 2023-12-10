class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_lists(head_1, head_2):
    pass

def list_to_values(head):
    pass

def test_add_lists():
    # Test 00
    a1, a2, a3 = Node(1), Node(2), Node(6)
    a1.next, a2.next = a2, a3
    b1, b2, b3 = Node(4), Node(5), Node(3)
    b1.next, b2.next = b2, b3
    assert list_to_values(add_lists(a1, b1)) == [5, 7, 9], "Test 00 failed"

    # Test 01
    a1, a2, a3, a4 = Node(1), Node(4), Node(5), Node(7)
    a1.next, a2.next, a3.next = a2, a3, a4
    b1, b2 = Node(2), Node(3)
    b1.next = b2
    assert list_to_values(add_lists(a1, b1)) == [3, 7, 5, 7], "Test 01 failed"

    # Test 02
    a1, a2 = Node(9), Node(3)
    a1.next = a2
    b1, b2 = Node(7), Node(4)
    b1.next = b2
    assert list_to_values(add_lists(a1, b1)) == [6, 8], "Test 02 failed"

    # Test 03
    a1, a2 = Node(9), Node(8)
    a1.next = a2
    b1, b2 = Node(7), Node(4)
    b1.next = b2
    assert list_to_values(add_lists(a1, b1)) == [6, 3, 1], "Test 03 failed"

    # Test 04
    a1, a2, a3 = Node(9), Node(9), Node(9)
    a1.next, a2.next = a2, a3
    b1 = Node(6)
    assert list_to_values(add_lists(a1, b1)) == [5, 0, 0, 1], "Test 04 failed"

    print("All tests passed!")

test_add_lists()
