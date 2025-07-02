# move zeros

def move_zeroes_brute_force(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(0, n -i - 1):
            if nums[j] == 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def move_zeroes_optimized_using_space(nums):
    n = len(nums)
    temp = []
    for i in range(0, n):
        if nums[i] != 0:
            temp.append(nums[i])
            
    for i in range(0, len(temp)):
        nums[i] = temp[i]
    
    for i in range(len(temp), n):
        nums[i] = 0
    # print(temp)
    
def move_zeroes_optimized(nums):
    n = len(nums)
    j = 0
    for i in range(0, n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j+=1
            
    
    
nums = [0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 12, 0, 100]
# move_zeroes_brute_force(nums)
# move_zeroes_optimized(nums)
move_zeroes_optimized_using_space(nums)
print(nums)