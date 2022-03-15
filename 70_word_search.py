''' Questions and Approach

    Input: board -> List[List[str]], word -> str
    Output: whether the word can be found in board -> boolean

    Given m x n board with characters inside, can we find the word inside the board?
    The character inside the board can only be used once, meaning each cell can be visited once to create the string
    The direction can only be up down left right.

    Constraints:
        1. Can there be empty board? And Board size?
            No empty board; 1 <= m, n <= 6
            edge case: 1x1 matrix
        2. Can there be empty word? And Word length?
            No empty word; 1 <= word.length <= 15
            edge case: word.length = 1
        3. Are the character inside board all letters?
            yes and lower case
        4. Are the character inside word all letters?
            yes and lower case

Depth First Search Approach:
    1. Base case:
        found the last match character (True)
        
        end of dfs (False)
            1. traverse out of bounds
            2. traverse to visited node
            3. too much character

        found not matching character (False)

Time Complexity:
    O(m * n * 3^word.length): m*n = cells 
        3^word.length
        we traverse 3 directions 
            we can safely assume that one of the direction is non valid by default
            because the question does not allow using the same cell (character)
        we only traverse till the word.length
    
Space Complexity:
    O(word.length)

'''

class Solution:
    def exist(self, board, word): # return boolean
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i = 0):

            if (i == len(word)):
                return True
            
            # visited
            if (r, c) in visited:
                return False

            # out of bounds:
            if (r < 0 or 
                c < 0 or 
                r >= ROWS or 
                c >= COLS):
                return False
            
            # not matching character
            if (word[i] != board[r][c]):
                return False
            
            # four direction: (up, down, left, right)

            visited.add((r, c))
            result = (dfs(r-1, c, i+1) or
            dfs(r+1, c, i+1) or
            dfs(r, c-1, i+1) or
            dfs(r, c+1, i+1))
            visited.remove((r, c))

            return result 

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, i = 0):
                    return True
        
        return False

''' Test Case

A B  word = AB; word = BDC word = D
C D

visited((1, 1))
dfs(r = 1, c = 1, i = 0)
dfs(r = 0, c = 1, i = 1) 

dfs(r = -1, c = 1, i = 2)


A B C (A B E H I)
D E F
G H I

Done:

    Edge Case:

    [[A]] word = B

    dfs(r = 0, c = 0, i = 0)
    dfs(r = -1, c = 0, i = 1)

'''