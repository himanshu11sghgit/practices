
# def quick_sort(arr, left, right):
#     if left < right:
#         ppost = partition(arr, left, right)
#         print(ppost)
#         quick_sort(arr, left, ppost-1)
#         quick_sort(arr, ppost+1, right)



# def partition(arr, left, right):
#     i = left
#     j = right-1
#     pivot = arr[right]

#     while (i<j):
#         while (i<right) and (arr[i] < pivot):
#             i+=1
#         while (j>left) and (arr[j] >= pivot):
#             j-=1

#         if (i<j):
#             arr[i], arr[j] = arr[i], arr[j]

#     if (arr[i] > pivot):
#         arr[i], arr[right] = arr[right], arr[i]

#     return i
