def greet(s):
    pass

def test_greet():
    assert greet("alvin") == "hey alvin", "Test failed for input 'alvin'"
    assert greet("jason") == "hey jason", "Test failed for input 'jason'"
    assert greet("how now brown cow") == "hey how now brown cow", "Test failed for input 'how now brown cow'"

    print("All tests passed!")

test_greet()
