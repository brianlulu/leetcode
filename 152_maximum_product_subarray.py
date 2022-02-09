class Solution:
    def maxProduct(self, nums):
        
        # input = [int]
        # output = int

        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            
            # edge case: 0
            if n == 0:
                curMax = 1
                curMin = 1
                res = max(0, res)
                continue
            
            
            #we need tmpMin because the curMin updated
            tmpMin = curMin
            curMin = min(tmpMin * n, curMax * n, n)
            curMax = max(tmpMin * n, curMax * n, n)

            res = max(res, curMax)

        
        return res
    
if __name__ == "__main__":

    s = Solution()
    r1 = s.maxProduct([2,3,-2,4])
    r2 = s.maxProduct([-2,0,-1])
    r3 = s.maxProduct([2,-5,-2,-4,3])

    print(r1, r2, r3)