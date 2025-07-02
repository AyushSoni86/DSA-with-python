# kadane's algo. maximum sum subarray

def find_max_sum_subarray(nums):
    maxi = float("-inf")
    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            maxi = max(maxi, sum)
    return maxi


def find_max_using_kadane_algo(nums):
    maxi = float("-inf")
    sum = 0
    for i in range(0, len(nums)):
        sum+=nums[i]
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0    
    return max

        



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = find_max_sum_subarray(nums)
res = find_max_using_kadane_algo(nums)
print(ans)
print(res)