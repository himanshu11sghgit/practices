nums = [20, 1, 2, 3, 1, 10, 5, 4, 10, 13, 21, 12, 2]



def selection_sort(nums):
    for i in range(0, len(nums), 1):
        mini = i
        for j in range(i+1, len(nums), 1):
            if nums[mini] > nums[j]:
                mini = j
        nums[mini], nums[i] = nums[i], nums[mini]





selection_sort(nums)
print(nums)


















































# def selection_sort(n):
#     for i in range(0, len(n)-1, 1):
#         index = i
#         for j in range(i+1, len(n), 1):
#             if n[index] > n[j]:
#                 index = j
#         n[i], n[index] = n[index], n[i]

#     return n


# print(selection_sort(nums))