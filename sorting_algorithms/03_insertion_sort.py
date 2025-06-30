def insertion_sort(nums):
    arr_len = len(nums)
    for i in range(1, arr_len):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j-=1
        nums[j + 1] = key


def insertion_sort_decending(nums):
    arr_len = len(nums)
    for i in range(1, arr_len):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


def insertion_sort_recursion(nums, n):
    if n <= 1:
        return
    insertion_sort_recursion(nums, n - 1)

    key = nums[n - 1]
    j = n - 2

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key


nums = [8, 3, 6, 5, 5, 8, 2, 3, 7, 6, 5, 5, 8]
print(nums)

# insertion_sort(nums)
# print(nums)

# insertion_sort_decending(nums)
# print(nums)

insertion_sort_recursion(nums, len(nums))
print(nums)