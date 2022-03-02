class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # input: text1 -> string, text2 -> string
        # output: length_of_longest_subsequence -> int

        # 2D array of 0s with size of length for both string. we add one more columns and rows of 0.
        # because our algorithm needs to search left and right cells for value
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1 , -1, -1):
                # add to common subseq
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                
        return dp[0][0]

        '''
        Time Complexity: O(len(text1) * len(text2))
        Space Complexity: O(len(text1) * len(text2))
        '''
    

if __name__ == "__main__":

    s = Solution()
    r1 = s.longestCommonSubsequence("abcde", "ace")

    print(r1)
