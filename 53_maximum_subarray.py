class Solution:
    def maxSubArray(self, nums):
        
        #input = [int]
        #output = [int]
    
        maxSum = nums[0] 
        curSum = 0

        for n in nums:
            
            if curSum < 0:
                curSum = 0
            
            curSum += n
            maxSum = max(curSum, maxSum)
        
        return maxSum

if __name__ == "__main__":

    s = Solution()
    r1 = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    r2 = s.maxSubArray([1])
    r3 = s.maxSubArray([5,4,-1,7,8])

    print(r1, r2, r3)

