from re import L


class Solution:
    def isValidSudoku(self, board):
        
        # input: List[List[str]]
        # ouput: boolean -> whether this is a valid sudoku

        # constraints:
        # board is always 9x9
        # board contains only digit 1-9 or '-'
        # we do not need to check for correctness for the sudoku 
        # just the valid state of current sudoku table

        # HashMap with HashSet Approach
        # use hashmap for the 3 different conditions check: cols, rows, sqaures
        # cols, rows (index of the cols or rows: hashset(1-9))
        # squares: we use a modified coordinate system to keep track the number belongs to which squares
        # for example, we know that digit at (4,4) (cols, rows) is belong to the square with coordinate of (4//3 = 1, 4//3 = 1)
        # for hashmap for the square (coordinate of square: hashset(1-9))

        cols, rows, squares = {}, {} , {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                # cols
                if j in cols:
                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])
                else:
                    cols[j] = set(board[i][j])

                # rows
                if i in rows:
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].add(board[i][j])
                else:
                    rows[i] = set(board[i][j])

                # squares
                squareCord = (i//3, j//3)
                if squareCord in squares:
                    if board[i][j] in squares[squareCord]:
                        return False
                    squares[squareCord].add(board[i][j])
                else:
                    squares[squareCord] = set(board[i][j])
                
        return True

        # TC: O(9^9)
        # SC: O(9^9) + O(9^9) + O(9^9) = O(9^9)
    

if __name__ == "__main__":

    s = Solution()
    r1 = s.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
    r2 = s.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

    print(r1)
    print(r2)

