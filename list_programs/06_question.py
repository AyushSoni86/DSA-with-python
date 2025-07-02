# rotate an array by k elements


def rotate_array_k_brute_force(nums, k):
    n = len(nums)
    rotations = k % n
    for i in range(0, rotations):
        removed = nums.pop()
        nums.insert(0, removed)
        
def rotate_array_k(nums, k):
    print('➡ list_programs/06_question.py:5 nums[:len(nums) - 1]:', nums[:len(nums) - k])
    print('➡ list_programs/06_question.py:5 nums[-k:]:', nums[-k:])
    if len(nums) == 1 or k == 0 or len(nums) == k: return
    nums[:] = nums[-(k%len(nums)):] + nums[:len(nums) - k%len(nums)]
    # nums[:] = nums[-k:] + nums[:len(nums) - k]


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1

def rotate_array_k_without_slicing(nums, k):
    n = len(nums)
    rotations = k % n
    reverse(nums, 0, n - rotations - 1)
    print('➡ list_programs/06_question.py:29 nums:', nums)
    reverse(nums, n - rotations, n - 1)
    print('➡ list_programs/06_question.py:29 nums:', nums)
    reverse(nums, 0, n - 1)
    print('➡ list_programs/06_question.py:29 nums:', nums)
     
    
     
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
rotate_array_k_without_slicing(nums, 4)
# print(nums)