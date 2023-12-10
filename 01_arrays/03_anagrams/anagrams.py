def anagrams(str1, str2):
    pass

def test_anagrams():
    assert anagrams('restful', 'fluster') == True, "Test failed for input 'restful', 'fluster'"
    assert anagrams('cats', 'tocs') == False, "Test failed for input 'cats', 'tocs'"
    assert anagrams('monkeyswrite', 'newyorktimes') == True, "Test failed for input 'monkeyswrite', 'newyorktimes'"
    assert anagrams('paper', 'reapa') == False, "Test failed for input 'paper', 'reapa'"
    assert anagrams('elbow', 'below') == True, "Test failed for input 'elbow', 'below'"
    assert anagrams('tax', 'taxi') == False, "Test failed for input 'tax', 'taxi'"
    assert anagrams('taxi', 'tax') == False, "Test failed for input 'taxi', 'tax'"
    assert anagrams('night', 'thing') == True, "Test failed for input 'night', 'thing'"
    assert anagrams('abbc', 'aabc') == False, "Test failed for input 'abbc', 'aabc'"
    assert anagrams('po', 'popp') == False, "Test failed for input 'po', 'popp'"
    assert anagrams('pp', 'oo') == False, "Test failed for input 'pp', 'oo'"

    print("All tests passed!")

test_anagrams()
