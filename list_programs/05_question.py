# rotate an array by 1 elements

def right_rotate(nums):
    nums[:] = [nums[-1]] + nums[0: len(nums) - 1]
    # return nums

def right_rotate_1(nums):
    temp = nums[-1]
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = temp

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
right_rotate_1(nums)
print(nums)