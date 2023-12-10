def uncompress(s):
    pass

def test_uncompress():
    assert uncompress("2c3a1t") == "ccaaat", "Test failed for input '2c3a1t'"
    assert uncompress("4s2b") == "ssssbb", "Test failed for input '4s2b'"
    assert uncompress("2p1o5p") == "ppoppppp", "Test failed for input '2p1o5p'"
    assert uncompress("3n12e2z") == "nnneeeeeeeeeeeezz", "Test failed for input '3n12e2z'"
    assert uncompress("127y") == "y" * 127, "Test failed for input '127y'"

    print("All tests passed!")

test_uncompress()
