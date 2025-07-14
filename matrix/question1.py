def printMatrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
    print()
    
def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    col = [0]*cols
    row = [0]*rows
    
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    
    for i in range(0, rows):
        for j in range(0, cols):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0             
   
def setZeroes_optimized(matrix):
    col0 = 1
    row0 = 1
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == 0:
                if j == 0: col0 = 0
                if i == 0: row0 = 0
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0             
    
    if row0 == 0:
        for i in range(0, cols):
            matrix[0][i] = 0
        
    if col0 == 0:
        for i in range(0, rows):
            matrix[i][0] = 0


matrix1 = [
    [1,1,1],
    [1,0,1],
    [1,1,1],
]
matrix2 = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5],
]

matrix3 = [[0,1]]

matrix4 = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [0, 10, 11, 12],
    [13, 14, 15, 0]
]

setZeroes_optimized(matrix1)
printMatrix(matrix1)

setZeroes_optimized(matrix2)
printMatrix(matrix2)

setZeroes_optimized(matrix3)
printMatrix(matrix3)

setZeroes_optimized(matrix4)
printMatrix(matrix4)