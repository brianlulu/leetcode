class Solution:
   
    def combinationSum(self, candidates, target):

        # input: candidates -> [int], target -> int
        # output: list of all the unique combination sum [[int]]

        result = []


        def dfs(i, curTarget, curComb):

            if curTarget == target:
                result.append(curComb.copy())
                return
            
            if (curTarget > target) or (i >= len(candidates)):
                return

            print(i, curComb, curTarget)


            # Traverse left
            curComb.append(candidates[i])
            dfs(i, curTarget + candidates[i], curComb)

            # BackTrack
            curComb.pop()
            # Traverse Right
            dfs(i+1, curTarget, curComb)

        dfs(0, 0, [])

        return result

if __name__ == "__main__":

    s = Solution()
    r1 = s.combinationSum(candidates = [2,3,5], target = 8)

    print(r1)
            

            

