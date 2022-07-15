from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # input: s -> str; k -> int
        # output: longest length of repeating character substring -> int

        # constraints:
        # s.length >= 1
        # k >= 0
        # s only constaints uppercase english

        # sliding windows + hashmap approach
        # we use the sliding window to construct the substring
        # use the hashmap to keep track the frequency of the character at current substring
        # move right pointer, if current window size - most frequent character in the substring <= k
        # move the left pointer, if above condition is not met

        freq = {} # character frequency hashmap {"A": 12}
        l = r = 0
        result = 0 # keep track the longest length
        maxFreq = 0

        if len(s) == 1:
            return 1

        while r < len(s):
            currWindowSize = len(s[l:r+1])
            
            freq[s[r]] = 1 + freq.get(s[r], 0)    
            maxFreq = max(freq.values()) 

            if currWindowSize - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            currWindowSize = len(s[l:r+1])
            r += 1
            result = max(result, currWindowSize)
        
        return result




if __name__ == "__main__":
    s = Solution()

    r1 = s.characterReplacement(s = "ABAB", k = 2)
    r2 = s.characterReplacement(s = "AABABBA", k = 1)

    print(r1)
    print(r2)



    """
    k = 2, currentWindow = 1

    "AAAA"
     
    ABAB
    L
     R

    k = 1
    substring = "BBB"
    AABABBA
      L
          R
    """