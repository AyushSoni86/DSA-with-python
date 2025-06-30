# find the largest element in an array

def find_largest(arr):
    largest = float("-inf")
    print(largest)
    max = arr[0]
    for i in range(0, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max

arr = [55, 32, -97, 99, 3, 27] 
print(find_largest(arr))
