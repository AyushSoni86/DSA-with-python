# fibonacci number using recursion
# 0 1 1 2 3 5 8 13 21 34
def fibo(n): 
    if n == 0 or n == 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(30))