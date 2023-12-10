def pair_sum(numbers, target):
    pass

def test_pair_sum():
    assert pair_sum([3, 2, 5, 4, 1], 8) == (0, 2), "Test failed for input [3, 2, 5, 4, 1], 8"
    assert pair_sum([4, 7, 9, 2, 5, 1], 5) == (0, 5), "Test failed for input [4, 7, 9, 2, 5, 1], 5"
    assert pair_sum([4, 7, 9, 2, 5, 1], 3) == (3, 5), "Test failed for input [4, 7, 9, 2, 5, 1], 3"
    assert pair_sum([1, 6, 7, 2], 13) == (1, 2), "Test failed for input [1, 6, 7, 2], 13"
    assert pair_sum([9, 9], 18) == (0, 1), "Test failed for input [9, 9], 18"
    assert pair_sum([6, 4, 2, 8], 12) == (1, 3), "Test failed for input [6, 4, 2, 8], 12"

    print("All tests passed!")

test_pair_sum()
