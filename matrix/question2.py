def printMatrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
    print()
    
def reverseArray(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i+=1
        j-=1
        
def rotate(matrix):
    n = len(matrix)
    for i in range(0, n):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]

    printMatrix(matrix)
    for i in range(0, n):
        reverseArray(matrix[i])

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

rotate(matrix1)
rotate(matrix2)

printMatrix(matrix1)
printMatrix(matrix2)