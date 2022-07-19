from curses.ascii import SO


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
        # input: matrix -> List[List[int]], target -> int
        # output: whether the target is in the matrix -> boolean

        # constraints:
        # m = matrix.length n = matrix[i].length
        # m, n >= 1

        # single binary search approach:
        # for iterate through every row in the matrix 
        # find the row such that the target is inside the row with
        # condition of row[0] <= target <= row[len(row)-1]

        # for row in matrix:
        #     l, r = 0, len(row) - 1
        #     if row[l] <= target <= row[r]:
        #         while l <= r:
        #             mid = (l+r)//2
        #             if row[mid] == target:
        #                 return True
        #             elif row[mid] > target:
        #                 r = mid - 1
        #             elif row[mid] < target:
        #                 l = mid + 1
        #         return False

        # return False

        # TC: O(M) + O(logN) where M = matrix.length and N = matrix[i].length
        # SC: O(1)

        # two binary search:
        # first use binary search to decide with row to search the target
        # then perform binary search on the row

        colL, colR = 0, len(matrix)-1

        while colL <= colR:
            colMid = (colL+colR)//2
            # first element of the current row is bigger than the target
            # find rows above it
            if target < matrix[colMid][0]: 
                colR = colMid - 1
            # last element of the current row is smaller than the target
            # find rows below it
            elif target > matrix[colMid][-1]:
                colL = colMid + 1
            # either target == last or first element of current row or in between
            else:
                break
        
        # the target > the largest number in matrix or the target < the smallest number in matrix
        if colL > colR:
            return False

        row = matrix[colMid]
        l , r = 0, len(row) - 1

        while l <= r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            elif row[mid] < target:
                l = mid + 1
        
        return False

        # TC: O(logM) + O(logN) where M = matrix.length and N = matrix[i].length
        # SC: O(1)



if __name__ == "__main__":

    s = Solution()
    r1 = s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
    r2 = s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)

    print(r1)
    print(r2)