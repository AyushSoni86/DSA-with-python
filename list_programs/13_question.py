# majority elements

def majorityElement(arr):
    majority_index = 0
    count = 1
    for i in range(0, len(arr)):
        if arr[i] == arr[majority_index]: count+=1
        else: count-=1
        if count == 0:
            majority_index = i
            count = 1
    majority_element = arr[majority_index]
    print('➡ list_programs/13_question.py:13 majority_element:', majority_element)
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == majority_element: count+=1
    
    if count > len(arr)/2:
        return majority_element
    else:
        return -1

nums =  [1, 1, 2, 1, 3, 5, 1, 2, 3]
print(majorityElement(nums))

       