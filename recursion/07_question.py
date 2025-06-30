# reverse an array in python without recursion
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        # swap the elements at start and end
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [1, 2, 3, 4, 5]
rev = arr[::-1]
# print(reverse_array(arr))
print(rev)

# reverse an array in python using recursion

def reverse_array_recursion(arr, start, end):
    if start >= end: 
        return arr
    # print(start, end, arr)
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_array_recursion(arr, start + 1, end - 1)
  

arr = [1, 2, 3, 4, 5]
print(reverse_array_recursion(arr, 0, len(arr) - 1))