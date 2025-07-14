def fourSum(nums):
    n = len(nums)
    my_set = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    answer = nums[i] + nums[j] + nums[k] + nums[l]
                    if answer == target:
                        temp_ans = [nums[i], nums[j], nums[k], nums[l]]
                        temp_ans.sort()
                        my_set.add(tuple(temp_ans))
    
    return [list(ans) for ans in my_set]

def fourSum_better(nums):
    n = len(nums)
    my_set = set()
    for i in range(n):
        for j in range(i + 1, n):
            my_dict = {}
            for k in range(j + 1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in my_dict and k != my_dict[fourth]:
                    temp_ans = [nums[i], nums[j], nums[k], fourth]
                    temp_ans.sort()
                    my_set.add(tuple(temp_ans))
                    
                my_dict[nums[k]] = k
    
    return [list(ans) for ans in my_set]


def foursum_optimized(nums):
    n = len(nums)
    nums.sort()
    result = []
    
    for i in range(0, n):
        if nums[i] == nums[i - 1] and i != 0: continue
        for j in range(i + 1, n):
            if nums[j] == nums[j - 1] and j > i + 1: continue
            k = j + 1
            l = n - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total > target:
                    l -= 1
                elif total < target:
                    k += 1
                else:
                    ans = [nums[i], nums[j], nums[k], nums[l]]
                    result.append(ans)
                    k+=1
                    l-=1
                    while nums[k] == nums[k - 1] and k < l: k += 1
                    while nums[l] == nums[l + 1] and k < l: l -= 1
                
    return result


nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums))
print(fourSum_better(nums))
print(foursum_optimized(nums))