def max_value(nums):
    pass

def test_max_value():
    assert max_value([4, 7, 2, 8, 10, 9]) == 10, "Test failed for input [4, 7, 2, 8, 10, 9]"
    assert max_value([10, 5, 40, 40.3]) == 40.3, "Test failed for input [10, 5, 40, 40.3]"
    assert max_value([-5, -2, -1, -11]) == -1, "Test failed for input [-5, -2, -1, -11]"
    assert max_value([42]) == 42, "Test failed for input [42]"
    assert max_value([1000, 8]) == 1000, "Test failed for input [1000, 8]"
    assert max_value([1000, 8, 9000]) == 9000, "Test failed for input [1000, 8, 9000]"
    assert max_value([2, 5, 1, 1, 4]) == 5, "Test failed for input [2, 5, 1, 1, 4]"

    print("All tests passed!")

test_max_value()
