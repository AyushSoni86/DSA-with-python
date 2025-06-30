def partitions(arr, low, high):
    pivot = arr[low]
    i, j = low, high
    
    while i < j:
        while(arr[i] <= pivot and i <= high - 1):
            i+=1
        while(arr[j] > pivot and j >= low + 1):
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        part_index = partitions(nums, low, high)
        quick_sort(nums, low, part_index - 1)
        quick_sort(nums, part_index + 1, high)




nums = [3, 6, 5, 5, 8, 2, 3, 7, 6, 5, 5, 8]
print(nums)
quick_sort(nums, 0, len(nums) - 1)
print(nums)
