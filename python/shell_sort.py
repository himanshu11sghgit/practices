nums = [20, 1, 2, 3, 1, 10, 5, 4, 10, 13, 21, 12, 2]


def shell_sort(arr):
    gap = len(arr)//2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while (j>=gap and arr[j-gap] > temp):
                arr[j] = arr[j-gap]
                j = j-gap
            arr[j] = temp
        gap = gap//2
        
    return arr


print(shell_sort(nums))
