def find_factors(num : int) -> list[int]:
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
                
    return result

def find_factors_optimized(num : int) -> list[int]:
    result = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)            
    return result

def find_factors_optimized_more(num : int) -> list[int]:
    result = []
    for i in range(1, int(num**0.5 + 1)):
        if num % i == 0:
            result.append(i)
            if i != num // i:
                result.append(num // i)
    return result

print(find_factors(100))
print(find_factors_optimized(100))
print(find_factors_optimized_more(100).sort())
