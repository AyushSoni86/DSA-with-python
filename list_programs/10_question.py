# find missing number

def find_missing_number(nums):
    i = 0
    count = 0
    while i < len(nums):
        count+=1
        correct = nums[i]
        if nums[i] == len(nums): 
            i+=1
            continue
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i+=1

    for j in range(0, len(nums)):
        if j != nums[j]: return j
            
nums = [9,6,4,2,3,5,7,0,1]
ans = find_missing_number(nums)
print(ans)