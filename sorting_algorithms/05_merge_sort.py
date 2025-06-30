# merge two sorted arrays
arr1 = [1, 2, 3, 5, 7, 9, 10, 11, 12, 13, 14]
arr2 = [2, 4, 6, 6, 8, 9]

def merge_two_sorted_arrays(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    
    i = j = 0
    result = []
    
    print(i, j)
    while(i < arr1_len and j < arr2_len):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    
    while(i < arr1_len): 
        result.append(arr1[i])
        i+=1

            
    while(i < arr1_len):
        result.append(arr2[j])
        j+=1
    
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    arr_left = arr[:mid]
    arr_right = arr[mid:]
    sorted_left = merge_sort(arr_left)
    sorted_right = merge_sort(arr_right)
    return merge_two_sorted_arrays(sorted_left, sorted_right)

nums = [8, 3, 6, 5, 5, 8, 2, 3, 7, 6, 5, 5, 8]
merge_sort(nums)
print(nums)
print(merge_two_sorted_arrays(arr1, arr2))
    
