class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        # input: matrix -> List[List[int]]
        # output: None
        
        row_zero = False
        rows, cols = len(matrix), len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                # update the first row and col to 0
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0: #row update columns
                    matrix[r][c] = 0
                
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
                
                
'''
TC : O(m * n)
SC : O(1)
'''
                
                    