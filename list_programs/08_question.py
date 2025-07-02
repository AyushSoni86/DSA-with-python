# linear search

def linear_search(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    return -1


arr = [55, 32, 97, -55, 45, 32, 88, 21, 97] 

ans = linear_search(arr, 320)
print(f"Element found at index: {ans}" if ans >= 0 else "Element not found")

