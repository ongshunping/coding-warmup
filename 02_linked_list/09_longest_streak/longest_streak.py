class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def longest_streak(head):
    pass

def test_longest_streak():
    # Test 00
    a, b, c, d, e, f = [Node(val) for val in [5, 5, 7, 7, 7, 6]]
    a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
    assert longest_streak(a) == 3, "Test 00 failed"

    # Test 01
    a, b, c, d, e, f = [Node(val) for val in [3, 3, 3, 3, 9, 9]]
    a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
    assert longest_streak(a) == 4, "Test 01 failed"

    # Test 02
    a, b, c, d, e, f = [Node(val) for val in [9, 9, 1, 9, 9, 9]]
    a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
    assert longest_streak(a) == 3, "Test 02 failed"

    # Test 03
    a, b = Node(5), Node(5)
    a.next = b
    assert longest_streak(a) == 2, "Test 03 failed"

    # Test 04
    a = Node(4)
    assert longest_streak(a) == 1, "Test 04 failed"

    # Test 05
    assert longest_streak(None) == 0, "Test 05 failed"

    print("All tests passed!")

test_longest_streak()
