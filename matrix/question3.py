def spiralOrder(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        col_start = 0
        row_start = 0
        col_end = cols
        row_end = rows
        ans = []
        while row_start < row_end and col_start < col_end:

            for i in range(col_start, col_end):
                if row_start < row_end:
                    ans.append(matrix[row_start][i])
            row_start += 1

            for i in range(row_start, row_end):
                if col_start < col_end:
                    ans.append(matrix[i][col_end - 1])
            col_end -= 1

            for i in range(col_end - 1, col_start - 1, -1):
                if row_start < row_end:
                    ans.append(matrix[row_end - 1][i])
            row_end -= 1

            for i in range(row_end - 1, row_start - 1, -1):
                if col_start < col_end:
                    ans.append(matrix[i][col_start])
            col_start += 1

        return ans
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(spiralOrder(matrix))
