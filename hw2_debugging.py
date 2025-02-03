import rand
import bubble_sort

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    half = len(arr)//2
    print("half = " + str(half))

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    print("left arr")
    print(left_arr)
    print("right arr")
    print(right_arr)
    
    if len(left_arr) == 0 and len(right_arr) == 0:
        return
    
    left_index = 0
    right_index = 0

    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            print(str(left_arr[left_index]) + " < " + str(right_arr[right_index]))
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            print(str(left_arr[left_index]) + " > " + str(right_arr[right_index]))
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
        print("while sorting array")
        print(merge_arr)

    for i in range(right_index, len(right_arr)):
        print(str(left_index + right_index))
        merge_arr[left_index + i] = right_arr[i]
        print("iterating over remainder of right array")
        print(merge_arr)

    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]
        print("iterating over remainder of left array")
        print(merge_arr)
        

    print(merge_arr)
    return merge_arr

arr = rand.random_array([None] * 20)
print(arr)
lil_arr = [0,6,3,9,2,0]
print(lil_arr)

arr_out = merge_sort(lil_arr)
print(arr_out)
arr_out = merge_sort(arr)
print(arr_out)

arr_out = bubble_sort.bubble_sort(lil_arr)
print(arr_out)
arr_out = bubble_sort.bubble_sort(arr)
print(arr_out)


