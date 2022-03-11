class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        # input: matrix -> List[List[int]]
        # output: None (rotate the matrix in place)
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0 , len(matrix) - 1 
        size = len(matrix)
        
        # n x n so we dont have to check top bottom
        while left < right: 
            
            # we only move n - 1 points
            # every iteration shrink the size of square by 2
            # b/c we updating l and r 
            # for example 
                # 4 * 4 move first 3
                # 2 * 2 move just 1
            # iterate through n - 1 times
            for i in range(size - 1):
                # TL -> TR
                tmpTR = matrix[top+i][right]
                matrix[top+i][right] = matrix[top][left + i]
                
                # TR -> BR
                tmpBR = matrix[bottom][right - i]
                matrix[bottom][right - i] = tmpTR
                
                # BR -> BL
                tmpBL = matrix[bottom - i][left]
                matrix[bottom - i][left] = tmpBR
                
                # BL -> TL
                matrix[top][left+i] = tmpBL
            
            left += 1
            right -= 1
            
            top += 1
            bottom -= 1
            
            size -= 2
                
'''
Time Complexity: O(n*n) we go through every cell
Space Complexity: O(1)
'''
                
                

#         [[1,2,3], top, bottom = 0, 2; left, right = 0, 2
#          [4,5,6],
#          [7,8,9]] i = 0 , 1, 2
        
#         [[7,4,1],
#          [8,5,2],
#          [9,6,3]]
        
#         i = 1;
#             tmpTR = m[1][2] = 6
#             m[1][2] = matrix[0][1] = 2
            
#             tmpBR = matrix[2][1] = 8
#             matrix[2][1] = tmpTR
            
#             tmpBL = matrix[1][0] = 4
#             matrix[1][0] = tmpBR = 8
            
#             matrix[0][1] = 4
        
        
#         [[1]] top = 0, bottom = 0 left = 0, right = 0
        
#         [[1,2], 
#          [3,4]] 
        
#         [[3,1], top = 0, bottom = 1, left = 0, right = 1
#          [4,2]]
        
#         i = 0; 
#             tmpTR = matrix[0][1] = 2
#             matrix[0][1] = matrix[0][0]
            
#             tmpBR = matrix[1][1] = 4
#             matrix[1][1] = 2
            
#             tmpBL = matrix[1][0] = 3
#             matrix[1][0] = tmpBR = 4
            
#             matrix[0][0] = 3
        
        
        
        
        
        
        
        
        
        
        