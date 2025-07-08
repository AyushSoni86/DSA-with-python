# length of longest consecutive sequence

# brute force solution
def find_sequence_bruteforce(nums):
    n = len(nums)
    longest_sequence = 0
    for i in range(0, n):
        curr_num = nums[i]
        count = 1
        while curr_num + 1 in nums:
            curr_num+=1
            count+=1
        longest_sequence = max(count, longest_sequence)
    return longest_sequence
    
# using sorting    
def find_sequence_using_sorting(nums):
    nums.sort()
    n = len(nums)
    count = 0
    last_smaller = float("-inf")
    longest_count = 0
    for i in range(0, n):
        num = nums[i]
        if num == nums[i - 1]:
            continue
        if num - 1 == last_smaller:
            count+=1
            last_smaller = num
        elif num - 1 != last_smaller:
            count=1
            last_smaller = num
        longest_count = max(count, longest_count)
        
    return longest_count

# using set   
def find_sequence_using_set(nums):
    n = len(nums)
    my_set = set(nums)
    longest = 0
    for num in my_set:
        if num - 1 not in my_set:
            count = 1
            curr_ele = num
            while curr_ele + 1 in my_set:
                count+=1
                curr_ele+=1
            longest = max(longest, count)
         
    return longest

nums = [1, 99, 101, 98, 2, 5, 3, 100, 100, 1, 1]
nums1 = [1,0,1,2]
print(find_sequence_bruteforce(nums))
print(find_sequence_using_sorting(nums))
print(find_sequence_using_set(nums))

print(find_sequence_bruteforce(nums1))
print(find_sequence_using_sorting(nums1))
print(find_sequence_using_set(nums1))

