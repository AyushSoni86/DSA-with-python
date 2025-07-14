# three sum problem

def threeSum(nums):
    n = len(nums)
    my_set = set()
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans = [nums[i], nums[j], nums[k]]
                    ans.sort()
                    my_set.add(tuple(ans))

    return [list(ans) for ans in my_set]


def threesum_optimized(nums):
    n = len(nums)
    result = set()
    for i in range(0, n):
        my_set = set()
        for j in range(i + 1, n):
            third = -(nums[i] + nums[j])
            if third in my_set:
                ans = [nums[i], nums[j], third]
                ans.sort()
                result.add(tuple(ans))
            my_set.add(nums[j])

    return [list(ans) for ans in result]


def threesum_more_optimized(nums):
    n = len(nums)
    nums.sort()
    result = []
    
    for i in range(0, n):
        if nums[i] == nums[i - 1] and i != 0: continue
        k = n - 1
        j = i + 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                ans = [nums[i], nums[j], nums[k]]
                result.append(ans)
                j+=1
                k-=1
                while nums[j] == nums[j - 1] and j < k: j += 1
                while nums[k] == nums[k + 1] and j < k: k -= 1
                
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(threesum_optimized(nums))
print(threesum_more_optimized(nums))