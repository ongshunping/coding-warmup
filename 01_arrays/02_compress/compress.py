def compress(s):
    pass

def test_compress():
    assert compress('ccaaatsss') == '2c3at3s', "Test failed for input 'ccaaatsss'"
    assert compress('ssssbbz') == '4s2bz', "Test failed for input 'ssssbbz'"
    assert compress('ppoppppp') == '2po5p', "Test failed for input 'ppoppppp'"
    assert compress('nnneeeeeeeeeeeezz') == '3n12e2z', "Test failed for input 'nnneeeeeeeeeeeezz'"
    assert compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy') == '127y', "Test failed for input '127y'"

    print("All tests passed!")

test_compress()
