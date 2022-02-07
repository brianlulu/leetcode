class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1 #left pointer as buy; right pointer as sell
        maxP = 0 # to record the max profix

        while r < len(prices):

            if prices[l] > prices[r]:
                # buy price is higher than the sell price
                l = r
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)

            r += 1
        
        return maxP
    
if __name__ == "__main__":

    s = Solution()

    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,1,3]))

