def frequency_map(arr: list[int]) -> dict:
    mapping = {}
    for i in range(0, len(arr)):
        if arr[i] in mapping:
            mapping[arr[i]] += 1
        else:
            mapping[arr[i]] = 1
    return mapping

def frequency_map_oneLiner(arr):
    hashmap = {}
    for i in range(0, len(arr)):
        hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1
    return hashmap

arr = [1, 2, 3, 3, 2, 5, 6, 3, 4, 5, 6, 8, 7, 6, 4, 3, 9]
dic1 = frequency_map(arr)
dic2 = frequency_map_oneLiner(arr)
print(dic1)
print(dic2)
