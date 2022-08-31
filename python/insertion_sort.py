nums = [22, 11, 88, 66, 55, 77, 33, 44]
nums2 = [20, 1, 2, 3, 1, 10, 5, 4, 10, 13, 21, 12, 2]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr





print(insertion_sort(nums2))

print(nums2)