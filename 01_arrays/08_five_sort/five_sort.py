def five_sort(nums):
    pass

def test_five_sort():
    assert five_sort([12, 5, 1, 5, 12, 7])[-2:] == [5, 5], "Test failed for input [12, 5, 1, 5, 12, 7]"
    assert five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])[-5:] == [5, 5, 5, 5, 5], "Test failed for input [5, 2, 5, 6, 5, 1, 10, 2, 5, 5]"
    assert five_sort([5, 5, 5, 1, 1, 1, 4])[-3:] == [5, 5, 5], "Test failed for input [5, 5, 5, 1, 1, 1, 4]"
    assert five_sort([5, 5, 6, 5, 5, 5, 5])[-6:] == [5, 5, 5, 5, 5, 5], "Test failed for input [5, 5, 6, 5, 5, 5, 5]"
    assert five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])[-8:] == [5, 5, 5, 5, 5, 5, 5, 5], "Test failed for input [5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]"

    print("All tests passed!")

test_five_sort()
