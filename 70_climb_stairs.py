class Solution:
    def climbStairs(self, n):

        # input: int
        # output: int

        # Recursion Method
        # if n == 0 or n == 1:
        #     return 1

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # DP Method
        # dp = [0] * (n+1)

        # for i in range(n+1):
        #     if i == 0:
        #         dp[i] = 1
        #     elif i == 1:
        #         dp[i] = 1
        #     else:
        #         dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        # Fibonacci
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one += two
            two = tmp
        
        return one

if __name__ == "__main__":

    s = Solution()
    r1 = s.climbStairs(5)
    print(r1)