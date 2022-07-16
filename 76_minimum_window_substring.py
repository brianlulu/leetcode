from re import L, S


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # input: s -> str; t -> str
        # output: the minimum substring window that contains all the string t

        # constraints:
        # s.length and t.length > 0
        # s and t consist lower and upper english letter

        # brute force method:
        # we find every possible substrings from s and 
        # check the minimum length of substrings from s that contains t
        # TC: O(n^2) + O(n^2)
        # SC: O(n^2)

        # slide window method:
        # use a sliding window to construct the substring from s
        # shift r pointer until s[l:r+1] includes everything in t
        # shift l pointer until s[l:r+1] does not includes everything in t
        # keep track of possible subtring and always choose the one with shortest length

        l = r = 0
        result = ""
        sCount, tCount = {}, {}

        if len(s) < len(t):
            return result

        for i in range(len(t)):
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
            sCount[t[i]] = 0
        
        need = len(tCount)
        have = 0
        minLength = 10**6

        while r < len(s):
            if s[r] in sCount:
                sCount[s[r]] += 1
                if sCount[s[r]] == tCount[s[r]]:
                    have += 1
            
            while need == have:
                if len(s[l:r+1]) < minLength:
                    result = s[l:r+1]
                    minLength = len(result)
                if s[l] in sCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                
                l += 1  
            r += 1

        return result

        # TC(2S) where S is the length of string s; worst case is that the right pointer travel to the end 
        # so is the left pointer

        # SC(2T + S) 2T for dictionary S is when the worst case that the whole string is used


if __name__ == "__main__":

    s = Solution()
    r1 = s.minWindow(s = "ADOBECODEBANC", t = "ABC")

    print(r1)







