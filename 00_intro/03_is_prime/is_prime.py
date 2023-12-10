def is_prime(n):
    pass

def test_is_prime():
    assert is_prime(2) == True, "Test failed for input 2"
    assert is_prime(3) == True, "Test failed for input 3"
    assert is_prime(4) == False, "Test failed for input 4"
    assert is_prime(5) == True, "Test failed for input 5"
    assert is_prime(6) == False, "Test failed for input 6"
    assert is_prime(7) == True, "Test failed for input 7"
    assert is_prime(8) == False, "Test failed for input 8"
    assert is_prime(25) == False, "Test failed for input 25"
    assert is_prime(31) == True, "Test failed for input 31"
    assert is_prime(2017) == True, "Test failed for input 2017"
    assert is_prime(2048) == False, "Test failed for input 2048"
    assert is_prime(1) == False, "Test failed for input 1"
    assert is_prime(713) == False, "Test failed for input 713"

    print("All tests passed!")

test_is_prime()
