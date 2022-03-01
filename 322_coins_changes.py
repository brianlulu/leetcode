class Solution:
    def coinChange(self, coins, amount):
        
        # input: coins -> [int]; amount -> int
        # output: minCoinCount: int

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for target in range(1, amount + 1): 
            for c in coins:
                if target - c >= 0:
                    dp[target] = min(1 + dp[target - c], dp[target])
        
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
        
    
    '''
    coins = [1,2,5]; amount = 11
    dp = [0,1,1,4,5...,12] index: 0-11

    target = 1; c = 1
    dp[1] = min(1+dp[0] = 1, dp[1]) = 1
    target = 1; c = 2 < 0
    target = 1; c = 5 < 0
    
    target = 2; c = 1 > 0
    dp[2] = min(1 + dp[1] = 2, dp[2] = 3) = 2
    target = 2; c = 2 > 0
    dp[2] = min(1+dp[0], dp[2] = 2) = 1
    target = 2; c = 5 < 0

    target = 11, c = 1 > 0
    dp[11] = min(1 + dp[10], dp[11]) = 1 + dp[10]
    target = 11, c = 2 > 0
    dp[11] = min(1 + dp[9], 1+dp[10]) = A
    target = 11, c = 5 > 0
    dp[11] = min(1 + dp[6], A) = B

    Time Complexity = O(amount * len(coins))
    Memory Complexity = O(amount + 1)

    '''

if __name__ == "__main__":

    s = Solution()
    r1 = s.coinChange([1,2,5], 11)
    r2 = s.coinChange([2], 3)

    print(r1, r2)