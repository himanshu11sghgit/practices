nums = [22, 11, 88, 66, 55, 77, 33, 44]
nums2 = [20, 1, 2, 3, 1, 10, 5, 4, 10, 13, 21, 12, 2]




def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index-1)
        quick_sort(arr, pivot_index+1, right)




# modify arr and return pivot index 
def partition(arr, left, right):
    i = left 
    j = right-1 
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
             arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i
    


quick_sort(nums2, 0, len(nums2)-1)
print(nums2)