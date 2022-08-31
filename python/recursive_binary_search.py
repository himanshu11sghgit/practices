nums = [1,2,3, 5, 7, 10, 11, 12, 15]
target = 8


def recursive_binary_search(n, t, l, r):
    if l>r:
        return False

    mid = (l+r)//2
    if n[mid] == t:
        return True
    elif n[mid] < t:
        return recursive_binary_search(n, t, mid+1, r)
    else:
        return recursive_binary_search(n, t, l, mid-1)




print(recursive_binary_search(nums, target, 0, len(nums)-1))