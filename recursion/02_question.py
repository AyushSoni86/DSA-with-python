def printNumber(n):
    if n == 1:
        return
    printNumber(n - 1)
    print(n)
    
printNumber(10)
