def intersection(a, b):
    pass


def test_intersection():
    assert sorted(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10])) == sorted([2, 6]), "Test failed for input [4, 2, 1, 6], [3, 6, 9, 2, 10]"
    assert sorted(intersection([2, 4, 6], [4, 2])) == sorted([2, 4]), "Test failed for input [2, 4, 6], [4, 2]"
    assert sorted(intersection([4, 2, 1], [1, 2, 4, 6])) == sorted([1, 2, 4]), "Test failed for input [4, 2, 1], [1, 2, 4, 6]"
    assert sorted(intersection([0, 1, 2], [10, 11])) == sorted([]), "Test failed for input [0, 1, 2], [10, 11]"

    print("All tests passed!")

test_intersection()
