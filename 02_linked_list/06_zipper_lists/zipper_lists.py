class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def zipper_lists(head_1, head_2):
    pass

def list_to_values(head):
    pass

def test_zipper_lists():
    # Test 00
    a, b, c = Node("a"), Node("b"), Node("c")
    x, y, z = Node("x"), Node("y"), Node("z")
    a.next, b.next, x.next, y.next = b, c, y, z
    assert list_to_values(zipper_lists(a, x)) == ["a", "x", "b", "y", "c", "z"], "Test 00 failed"

    # Test 01
    a, b, c, d, e, f = Node("a"), Node("b"), Node("c"), Node("d"), Node("e"), Node("f")
    x, y, z = Node("x"), Node("y"), Node("z")
    a.next, b.next, c.next, d.next, e.next, x.next, y.next = b, c, d, e, f, y, z
    assert list_to_values(zipper_lists(a, x)) == ["a", "x", "b", "y", "c", "z", "d", "e", "f"], "Test 01 failed"

    # Test 02
    s, t = Node("s"), Node("t")
    one, two, three, four = Node(1), Node(2), Node(3), Node(4)
    s.next, one.next, two.next, three.next = t, two, three, four
    assert list_to_values(zipper_lists(s, one)) == ["s", 1, "t", 2, 3, 4], "Test 02 failed"

    # Test 03
    w = Node("w")
    one, two, three = Node(1), Node(2), Node(3)
    one.next, two.next = two, three
    assert list_to_values(zipper_lists(w, one)) == ["w", 1, 2, 3], "Test 03 failed"

    # Test 04
    one, two, three = Node(1), Node(2), Node(3)
    w = Node("w")
    one.next, two.next = two, three
    assert list_to_values(zipper_lists(one, w)) == [1, "w", 2, 3], "Test 04 failed"

    print("All tests passed!")

test_zipper_lists()
