# remove duplicates from an array

def removeDuplicates_bruteforce(arr):
    hashmap = {}
    for i in range(0, len(arr)):
        hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1
    return hashmap.keys()
        


def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[j] = nums[i]
            j+=1
            
    return j - 1;       

def removeDuplicates_optimal(nums):
    if(len(nums) == 1): return 1
    i = 0
    j = i + 1
    while j < len(nums):
        if(nums[i] != nums[j]):
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
        j+=1
    return i + 1

arr = [2, 3, 3, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8]
print(removeDuplicates_optimal(arr))
print(arr)