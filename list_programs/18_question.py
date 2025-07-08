# two sums

def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_1(nums, target):
    map = {}
    for i in range(0, len(nums)):
        map[nums[i]] = i   
    for i in range(0, len(nums)): 
        compliment = target - nums[i]
        if compliment in map and i != map[compliment]:
            return [i, map[compliment]]
            
    return []

def two_sum_1(nums, target):
    map = {}
    for i in range(0, len(nums)):
        compliment = target - nums[i]
        if compliment in map and i != map[compliment]:
            return [i, map[compliment]]
        map[nums[i]] = i   
            
    return []

nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6

print(two_sum_1(nums1, target1))
print(two_sum_1(nums2, target2))
print(two_sum_1(nums3, target3))




