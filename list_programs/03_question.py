# check if array is sorted or not


def is_sorted(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
        
        
arr1 = [2, 3, 3, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8]
arr2 = [55, 32, 97, -55, 45, 32, 88, 21, 97] 
print(is_sorted(arr1))
print(is_sorted(arr2))