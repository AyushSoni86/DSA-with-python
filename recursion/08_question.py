# check if str1ing is palindrome or not using recursion and normal loops both



def is_plaindrome_iterations(str, start, end):
    while(start < end):
        if str[start] != str[end]:
            return False
        start+=1
        end-=1
    return True

def is_plaindrome_recursion(str, start, end):
    if start >= end:
        return True
    if str[start] != str[end]:
        return False
    return is_plaindrome_recursion(str, start + 1, end - 1)

str = "nitinn"
print(is_plaindrome_iterations(str, 0,  len(str) - 1))
print(is_plaindrome_recursion(str, 0,  len(str) - 1))
    
