class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_lists(head_1, head_2):
    pass

def list_to_values(head):
    pass

def test_merge_lists():
    # Test 00
    a, b, c, d, e, f = [Node(val) for val in [5, 7, 10, 12, 20, 28]]
    q, r, s, t = [Node(val) for val in [6, 8, 9, 25]]
    a.next, b.next, c.next, d.next, e.next, q.next, r.next, s.next = b, c, d, e, f, r, s, t
    assert list_to_values(merge_lists(a, q)) == [5, 6, 7, 8, 9, 10, 12, 20, 25, 28], "Test 00 failed"

    # Test 01
    a, b, c, d, e, f = [Node(val) for val in [5, 7, 10, 12, 20, 28]]
    q, r, s, t = [Node(val) for val in [1, 8, 9, 10]]
    a.next, b.next, c.next, d.next, e.next, q.next, r.next, s.next = b, c, d, e, f, r, s, t
    assert list_to_values(merge_lists(a, q)) == [1, 5, 7, 8, 9, 10, 10, 12, 20, 28], "Test 01 failed"

    # Test 02
    h = Node(30)
    p, q = Node(15), Node(67)
    p.next = q
    assert list_to_values(merge_lists(h, p)) == [15, 30, 67], "Test 02 failed"

    print("All tests passed!")

test_merge_lists()
