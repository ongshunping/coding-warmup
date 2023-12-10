class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_univalue_list(head):
    pass

def test_is_univalue_list():
    # Test 00
    a = Node(7)
    b = Node(7)
    c = Node(7)
    a.next = b
    b.next = c
    assert is_univalue_list(a) == True, "Test 00 failed"

    # Test 01
    a = Node(7)
    b = Node(7)
    c = Node(4)
    a.next = b
    b.next = c
    assert is_univalue_list(a) == False, "Test 01 failed"

    # Test 02
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)
    u.next = v
    v.next = w
    w.next = x
    x.next = y
    assert is_univalue_list(u) == True, "Test 02 failed"

    # Test 03
    u = Node(2)
    v = Node(2)
    w = Node(3)
    x = Node(3)
    y = Node(2)
    u.next = v
    v.next = w
    w.next = x
    x.next = y
    assert is_univalue_list(u) == False, "Test 03 failed"

    # Test 04
    z = Node('z')
    assert is_univalue_list(z) == True, "Test 04 failed"

    print("All tests passed!")

test_is_univalue_list()
