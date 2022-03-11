class Solution:
    def spiralOrder(self, matrix):
        
        # input: matrix -> List[List[int]]
        # output: all element in matrix in spiral order -> List[int]

        result = []
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        print("First initail(left, right, top, bottom):")
        print(left, right, top, bottom)
        
        # travel four direction
        while left < right and top < bottom:
            
            # left to right and update top
            for i in range(left, right): # l = 0, r = 1
                result.append(matrix[top][i]) # matrix[0][0] = 1
            top += 1
            
            print("l to r direction(left, right, top, bottom):")
            print(left, right, top, bottom)
        
            # top to bottom and update right
            for j in range(top, bottom): # t = 1 , b = 3
                result.append(matrix[j][right-1]) # matrix[1][0] # matrix[2][0]
            right -= 1
            
            if top >= bottom or left >= right:
                break
            
            print("t to b direction(left, right, top, bottom):")
            print(left, right, top, bottom)
            
            # right to left and update bottom
            for k in range(right - 1, left - 1, -1):
                result.append(matrix[bottom-1][k])
            bottom -= 1
            
            print("r to l direction(left, right, top, bottom):")
            print(left, right, top, bottom)
            
            # bottom to up and update left
            for l in range(bottom - 1, top - 1, -1):
                result.append(matrix[l][left])
            left += 1
            
            print("b to u direction(left, right, top, bottom):")
            print(left, right, top, bottom)
            
        return result
    
    '''
    Time Complexity: O(m x n) iterate through every element in matrix
    Space Complexity: O(m x n) we keep our result 
    '''