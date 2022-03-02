class Solution:
    def wordBreak(self, s, wordDict):
        
        # input: s -> str, wordDict -> [str]
        # output: wether the words in wordDict can made up the string s -> Boolean

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1 ,-1):
            for word in wordDict:
                # word is in substring
                if i + len(word) <= len(s) and s[i: i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                # word is not
                if dp[i]:
                    break
        
        return dp[0]

        '''
        Time Complexity: O(N*M) where N = len(s), M = len(wordDict)
        Space Complexity: O(N)
        '''

if __name__ == "__main__":

    s = Solution()
    r1 = s.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
    
    print(r1)