# max consecutive ones
def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count+=1
        else:
            count=0
        max_count = max(max_count, count)
    return max_count


nums1 = [0, 1, 0, 1, 1, 1, 1]

nums2 = [0, 0, 1, 0, 1, 0]

nums3 = [0, 0, 0, 0]

# nums1 = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums1))
print(findMaxConsecutiveOnes(nums2))
print(findMaxConsecutiveOnes(nums3))