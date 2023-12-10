def pair_product(numbers, target):
    pass

def test_pair_product():
    assert pair_product([3, 2, 5, 4, 1], 8) == (1, 3), "Test failed for input [3, 2, 5, 4, 1], 8"
    assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2), "Test failed for input [3, 2, 5, 4, 1], 10"
    assert pair_product([4, 7, 9, 2, 5, 1], 5) == (4, 5), "Test failed for input [4, 7, 9, 2, 5, 1], 5"
    assert pair_product([4, 7, 9, 2, 5, 1], 35) == (1, 4), "Test failed for input [4, 7, 9, 2, 5, 1], 35"
    assert pair_product([4, 6, 8, 2], 16) == (2, 3), "Test failed for input [4, 6, 8, 2], 16"

    print("All tests passed!")

test_pair_product()
