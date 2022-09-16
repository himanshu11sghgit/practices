nums = [1,2,3, 5, 7, 10, 11, 12, 15]
target = 111


def binary_search(nums):
    l = 0
    r = len(nums)-1

    while (l <= r):
        mid = (l+r)//2
        if (nums[mid] == target):
            return True
        elif (nums[mid] < target):
            l = mid + 1
        else:
            r = mid - 1

    return False




print(binary_search(nums))










































# def iterative_binary_search(n, t):
#     l = 0
#     r = len(n)-1
#     while l<=r:
#         mid = (l+r)//2
#         if n[mid] == t:
#             return True
#         elif n[mid] < t:
#             l = mid+1
#         else:
#             r = mid-1

#     return False



# print(iterative_binary_search(nums, target))
