def bubble_sort(arr):
    count = 0
    while count < len(arr):
        index = 0
        while index < len(arr) - 1 - count:
            if arr[index] > arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp
            index = index + 1
        count = count + 1
    return arr
