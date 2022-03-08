class Solution:
    def numIslands(self, grid):
        
        # input: grid -> List[ List[str] ]
        # output: total numbers of islands -> int

        rows, cols = len(grid), len(grid[0])
        result = 0
        visited = set()

        # bfs function (queues implementation)
        def bfs(r, c):
            queue = []

            # add the current cell to queue
            queue.append((r, c))

            # mark current cell to visited
            visited.add((r, c))
            
            while queue:
                cur_r, cur_c = queue.pop(0)
                # traverse four directions
                for dr, dc in [(-1,0), (1, 0), (0, -1), (0, 1)]: 
                    next_r, next_c = cur_r + dr, cur_c + dc
                    # check if the next cell we traverse are out of index or not a land or visited
                    if ((next_r, next_c) not in visited and next_r < rows and next_c < cols and 
                        next_r >= 0 and next_c >= 0 and grid[next_r][next_c] == "1"):
                        queue.append((next_r, next_c))
                        visited.add((next_r, next_c))
                

        # iterate through every cell
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    result += 1

        return result

        '''
        Time Complexity: O(mn) check every cell, even we use bfs we marked the visited cell
        Space Complexity: O(mn) we use hashset to keep check the visited cell, 
            the worst case is that it is all "1" inside the grid
        '''


if __name__ == "__main__":

    s = Solution()
    r1 = s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])

    print(r1)