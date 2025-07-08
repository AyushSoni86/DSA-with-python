# rainwater trapping problem

def trapped_water(nums):
    n = len(nums)
    left = [nums[0]]
    right = [nums[n - 1]]
    trapped_water = 0
    
    for i in range(1, n):
        if nums[i] < left[i - 1]:
            left.append(left[i - 1])
        else: left.append(nums[i])
        
    for i in range(0, n - 1):
        if nums[n - i - 2] < right[i]:
            right.append(right[i])
        else: right.append(nums[n - i - 2])
    
    right.reverse()
    
    print(left)
    print(right)
    
    for i in range(0, n):
        trapped_water += min(left[i], right[i])  - nums[i]
       
        
    return trapped_water
    


nums = [3,1,2,4,0,1,3,2]
print(trapped_water(nums))