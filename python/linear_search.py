nums = [1,2,3, 5, 7, 10, 11, 12, 15]
target = 30

def linear_search(n, t):
    for i in range(0, len(n), 1):
        if n[i] == t:
            return True
        
    return False


print(linear_search(nums, target))