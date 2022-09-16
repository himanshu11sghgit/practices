nums = [20, 1, 2, 3, 1, 10, 5, 4, 10, 13, 21, 12, 2]



def bubble_sort(nums):
    for i in range(len(nums), 1, -1):
        for j in range(1, i, 1):
            if (nums[j-1] > nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]


bubble_sort(nums)
print(nums)














































# def bubble_sort(n):
#     for i in range(len(n)-1, 0, -1):
#         for j in range(0, i, 1):
#             if n[j] > n[j+1]:
#                 n[j], n[j+1] = n[j+1], n[j] 
            
#     return n


# print(bubble_sort(nums))