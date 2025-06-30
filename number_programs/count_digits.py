from math import log10

def count_digits(num: int):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count 

def count_digits_usinglog(num : int):
    if num < 10:
        return 1
    return int(log10(num)) + 1


print(count_digits(123456))
print(count_digits_usinglog(123456))