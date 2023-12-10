class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(values):
    pass

def list_to_values(head):
    pass

def test_create_linked_list():
    # Test 00
    assert list_to_values(create_linked_list(["h", "e", "y"])) == ["h", "e", "y"], "Test 00 failed"

    # Test 01
    assert list_to_values(create_linked_list([1, 7, 1, 8])) == [1, 7, 1, 8], "Test 01 failed"

    # Test 02
    assert list_to_values(create_linked_list(["a"])) == ["a"], "Test 02 failed"

    # Test 03
    assert create_linked_list([]) is None, "Test 03 failed"

    print("All tests passed!")

test_create_linked_list()
