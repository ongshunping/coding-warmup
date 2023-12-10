def most_frequent_char(s):
    pass

def test_most_frequent_char():
    assert most_frequent_char('bookeeper') == 'e', "Test failed for input 'bookeeper'"
    assert most_frequent_char('david') == 'd', "Test failed for input 'david'"
    assert most_frequent_char('abby') == 'b', "Test failed for input 'abby'"
    assert most_frequent_char('mississippi') == 'i', "Test failed for input 'mississippi'"
    assert most_frequent_char('potato') == 'o', "Test failed for input 'potato'"
    assert most_frequent_char('eleventennine') == 'e', "Test failed for input 'eleventennine'"
    assert most_frequent_char('riverbed') == 'r', "Test failed for input 'riverbed'"

    print("All tests passed!")

test_most_frequent_char()
