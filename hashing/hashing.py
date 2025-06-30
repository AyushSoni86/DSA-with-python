# hashing - prestore values n some datastructure like list/dict/sets and then fetching it
arr_num = [1, 2, 1, 6, 3, 7, 0, 3, 5, 7, 9, 4, 3, 5, 7, 9, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_num_check = [1, 2, 3, 4, 5, 6, 7, 56]

frequency_map = {}
for i in range(0, len(arr_num)):
    if arr_num[i] in frequency_map:
        frequency_map[arr_num[i]] += 1
    else:
        frequency_map[arr_num[i]] = 1
        
print(frequency_map)