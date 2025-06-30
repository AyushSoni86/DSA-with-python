# find the second largest element in an array

# time complexiety: O(2n)
def find_second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in range(0, len(arr)):
        if largest < arr[i]:
            largest = arr[i]
    for i in range(0, len(arr)):
        if second_largest < arr[i] and arr[i] != largest:
            second_largest = arr[i]
    return largest, second_largest

# time complexiety: O(n)
def find_second_largest_optimal(arr):
    largest = arr[0]
    second_largest = arr[0]
    for i in range(0, len(arr)):
        if largest < arr[i]:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return largest, second_largest

arr = [55, 32, 97, -55, 45, 32, 88, 21, 97] 
print(find_second_largest(arr))
print(find_second_largest_optimal(arr))
