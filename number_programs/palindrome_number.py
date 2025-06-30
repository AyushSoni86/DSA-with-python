num = 123211

def isPalindrome(num : int) -> bool:
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        num //= 10
        rev = rev*10 + digit
        
    return original == rev

print(isPalindrome(num))
        