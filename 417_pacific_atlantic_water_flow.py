class Solution:
    def pacificAtlantic(self, heights):
        
        #input: heights -> [[int]]
        #output: cords of cell that can reach both oceans -> [[int]]

        row, col = len(heights), len(heights[0])

        pac_cord = set()
        alt_cord = set()

        def dfs(r, c, visited, preHeight):

            # r: row -> int; c: column -> int
            # visited: visited cords -> set(); preHeight: the height from the previous cell -> int

            # constraints: out of index, current height < previous height
            if r >= len(heights) or c >= len(heights[0]) or r < 0 or c < 0 or heights[r][c] < preHeight or (r, c) in visited:
                return
            
            # add the cord to visited
            visited.add((r, c))

            # traverse for direction
            # up
            dfs(r-1, c, visited, heights[r][c])

            # down
            dfs(r+1, c, visited, heights[r][c])

            # left
            dfs(r, c-1, visited, heights[r][c])

            # right
            dfs(r, c+1, visited, heights[r][c])

        # iterate through the first and last row
        for c in range(col):
            # pacific boarder
            dfs(0, c, pac_cord, heights[0][c])
            # atlantic boarder
            dfs(row - 1, c, alt_cord, heights[row-1][c])

        # iterate through the first and last columns
        for r in range(row):
            # pacific boarder
            dfs(r, 0, pac_cord, heights[r][0])

            # atlantic boarder
            dfs(r, col-1, alt_cord, heights[r][col-1])
        
        return [list(cord) for cord in alt_cord.intersection(pac_cord)]
    
    '''
    Time complexity: O(mn) for dfs worst case is that the value inside of every cell is the same value
    Space complexity: O(mn) for every cell inside the set
    '''

if __name__ == "__main__":

    s = Solution()
    r1 = s.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    r2 = s.pacificAtlantic(heights = [[2,1],[1,2]])

    print(r1)
    print(r2)