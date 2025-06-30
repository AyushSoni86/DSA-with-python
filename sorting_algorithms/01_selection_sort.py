def selection_sort(arr):
    arr_len = len(arr)
    for i in range(0, arr_len):
        min_index = i
        for j in range(i+1, arr_len):
            if arr[min_index] > arr[j]:
                min_index = j               
        arr[min_index], arr[i] = arr[i], arr[min_index]
   
   
def selection_sort_decending(arr):
    arr_len = len(arr)
    for i in range(0, arr_len):
        max_index = i
        for j in range(i+1, arr_len):
            if arr[max_index] < arr[j]:
                max_index = j               
        arr[max_index], arr[i] = arr[i], arr[max_index]
     
def selection_sort_recursive(arr, start=0):
    if start >= len(arr) - 1:
        return

    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i

    arr[start], arr[min_index] = arr[min_index], arr[start]
    
    selection_sort_recursive(arr, start + 1)

                
arr = [8, 3, 6, 5, 5, 8, 2, 3, 7, 6, 5, 5, 8]
print(arr)
selection_sort(arr)
print(arr)
selection_sort_decending(arr)
print(arr)
selection_sort_recursive(arr, 0)
print(arr)