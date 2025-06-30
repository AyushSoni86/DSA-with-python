# rotate an array by k elements

def rotate_array_k(nums, k):
    print('➡ list_programs/06_question.py:5 nums[:len(nums) - 1]:', nums[:len(nums) - k])
    print('➡ list_programs/06_question.py:5 nums[-k:]:', nums[-k:])
    nums[:] = nums[-k:] + nums[:len(nums) - k]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
rotate_array_k(nums, 4)
print(nums)