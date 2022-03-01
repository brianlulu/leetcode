class Solution:
    def lengthOfLIS(self, nums):
        
        # input = nums -> [int]
        # output = longest subsequence length -> int

        dp = [1] * len(nums) # minimum of subsequence is itself (1)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

    '''
    nums = [0,1,0,3,2,3]
    dp =   [1,1,3,1,2,1]

    i = 5, j = 6 dp[5] = 1
    i = 4, j = 5
        nums[4] = 2 < nums[5] = 3
            dp[4] = max(dp[4] = 1, 1+dp[5] = 2) = 2
    i = 3, j = 4
        nums[3] = 3 > nums[4] = 2 # false
    i = 3, j = 5
        nums[3] = 3 = nums[5] = 3 # false

    i = 2, j = 3
        nums[2] = 0 < nums[3] = 3
            dp[2] = max(dp[2] = 1, 1+dp[3] = 2) = 2
    i = 2, j = 4
        nums[2] = 0 < nums[4] = 2
            dp[2] = max(dp[2] = 2, 1+dp[4] = 3) = 3
    i = 2, j = 5
        nums[2] = 0 < nums[5] = 3
            dp[2] = max(dp[2] = 3, 1+dp[5] = 2) = 3
    
    i = 1, j= 2
        nums[1] = 1 > nums[2] = 0  #false
    i = 1, j = 3
        nums[1] = 1 < nums[3] = 3
            dp[1] = max(dp[1] = 1, 1+dp[3] = 2)
 
    Time Complexity: O(n^2) 
        n = check from last element to the first element 
        n - 1 = check every elements after the index 
        first loop to the 0 index and the second loop from 1 -> n
    
    Space Complexity: O(n)
        dp array
    '''

if __name__ == "__main__":

    s = Solution()
    r1 = s.lengthOfLIS([0,1,0,3,2,3])

    print(r1)