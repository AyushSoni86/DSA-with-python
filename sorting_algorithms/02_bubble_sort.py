def bubble_sort(nums):
    arr_len = len(nums)
    for i in range(0, arr_len):
        for j in range(0, arr_len - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1] , nums[j] = nums[j] , nums[j + 1]

def bubble_sort_decending(nums):
    arr_len = len(nums)
    for i in range(0, arr_len):
        for j in range(0, arr_len - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j + 1] , nums[j] = nums[j] , nums[j + 1]

def bubble_sort_recursion(nums, start):
    if start > len(nums):
        return
    for j in range(0, len(nums) - start - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1] , nums[j] = nums[j] , nums[j + 1]
                
    bubble_sort_recursion(nums, start + 1)

nums = [8, 3, 6, 5, 5, 8, 2, 3, 7, 6, 5, 5, 8]
print(nums)

bubble_sort(nums)
print(nums)

bubble_sort_decending(nums)
print(nums)

bubble_sort_recursion(nums, 0)
print(nums)