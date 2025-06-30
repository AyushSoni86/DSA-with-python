# sum of n natural numbers

def sumOfNum(sum, num):
    if num == 0:
        print(sum)
        return
    sum = sum + num
    sumOfNum(sum, num - 1)
    
sumOfNum(0, 5)