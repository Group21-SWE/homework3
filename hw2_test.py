from hw2_debugging import merge_sort

def test_usual():
    input_arr = [i for i in range(5,0,-1)]
    actual_outcome = merge_sort(input_arr)
    expected_outcome = [1,2,3,4,5]
    assert actual_outcome == expected_outcome

def test_one_element():
    input_arr = [0]
    actual_outcome = merge_sort(input_arr)
    expected_outcome = [0]
    assert actual_outcome == expected_outcome

def test_non_element():
    input_arr = []
    actual_outcome = merge_sort(input_arr)
    expected_outcome = []
    assert actual_outcome == expected_outcome