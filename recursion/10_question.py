# count the number of ways to reach the destination

def count_paths(m, n):
    if m == 1 or n == 1: return 1
    return count_paths(m - 1, n) + count_paths(n, m - 1)
    
    
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(count_paths(3, 3))