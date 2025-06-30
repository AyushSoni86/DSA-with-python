from math import *
def armstrong_number(num : int) -> bool:
    size = int(log10(num) + 1)
    original = num
    result = 0
    while num > 0:
        digit = num % 10
        num //= 10 
        result += digit**size
    return result == original

print(armstrong_number(153))
print(armstrong_number(1))
print(armstrong_number(2))
print(armstrong_number(27))
print(armstrong_number(1634))
