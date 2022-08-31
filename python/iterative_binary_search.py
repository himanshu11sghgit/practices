nums = [1,2,3, 5, 7, 10, 11, 12, 15]
target = 11


def iterative_binary_search(n, t):
    l = 0
    r = len(n)-1
    while l<=r:
        mid = (l+r)//2
        if n[mid] == t:
            return True
        elif n[mid] < t:
            l = mid+1
        else:
            r = mid-1

    return False



print(iterative_binary_search(nums, target))
