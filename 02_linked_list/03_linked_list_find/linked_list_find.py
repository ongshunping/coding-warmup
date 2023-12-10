class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_find(head, target):
    pass

def test_linked_list_find():
    # Test 00
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    assert linked_list_find(a, "c") == True, "Test 00 failed"

    # Test 01
    a.next = b
    b.next = c
    c.next = d
    assert linked_list_find(a, "d") == True, "Test 01 failed"

    # Test 02
    a.next = b
    b.next = c
    c.next = d
    assert linked_list_find(a, "q") == False, "Test 02 failed"

    # Test 03
    node1 = Node("jason")
    node2 = Node("leneli")
    node1.next = node2
    assert linked_list_find(node1, "jason") == True, "Test 03 failed"

    # Test 04
    node1 = Node(42)
    assert linked_list_find(node1, 42) == True, "Test 04 failed"

    # Test 05
    node1 = Node(42)
    assert linked_list_find(node1, 100) == False, "Test 05 failed"

    print("All tests passed!")

test_linked_list_find()
