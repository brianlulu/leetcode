from re import L


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # input: s1 -> string; s2 -> string
        # output: whether s2 contains of s1's permutation

        # constraints:
        # s1.length, s2.length >= 1
        # s1 and s2 only contains lower english letters



        """sorted approach: (TLE)
        sorted s1 and sort substring of s2 and use set to look for the intersection for both string
        TC  O(nlogn) + O(n) where n is the longer string length
        SC O(1)


        newS1 = sorted(s1)
        l, r = 0, len(s1)-1

        if len(s1) > len(s2):
            return False
        
        while r < len(s2):
            curSubstring = sorted(s2[l:r+1])
            if curSubstring == newS1:
                return True
            
            l += 1
            r += 1
        
        return False
        """

        # slide window + hashmap approach:
        # we use sliding window size of s1 to slide through s2; 
        # use hashmaps with keys a-z to keep track the frequency of the character for s1 and window of s2
        # then use a variable "matches" to keep track that s1 and sliding window of s2 matches (26 means matched)
        # the two hashmap matches means that they both have same frequency for character counts

        l, r = 0, len(s1) - 1
        s1Count, s2Count = [0] * 26, [0] * 26
        match = 0
        
        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                match += 1
        
        while r < len(s2) - 1:
            if match == 26:
                return True
            
            s2Count[ord(s2[l]) - ord('a')] -= 1
            
            if s2Count[ord(s2[l]) - ord('a')] == s1Count[ord(s2[l]) - ord('a')]:
                match += 1
            elif s2Count[ord(s2[l]) - ord('a')] + 1 == s1Count[ord(s2[l]) - ord('a')]: 
            # the only time match decrease, its when there was a match and become doesnt match
            # meaning when there wasnt a match, the match should not change Therefore we cannot use else here
                match -= 1

            r += 1
            s2Count[ord(s2[r]) - ord('a')] += 1

            if s2Count[ord(s2[r]) - ord('a')] == s1Count[ord(s2[r]) - ord('a')]:
                match += 1
            elif s2Count[ord(s2[r]) - ord('a')] == s1Count[ord(s2[r]) - ord('a')] + 1: 
                match -= 1

            l += 1

        if match == 26:
            return True

        return False

        # TC: O(26) + O(s2.length - s1.length) 
        # SC: O(26) 



if __name__ == "__main__":


    s = Solution()
    
    # r1 = s.checkInclusion(s1 = "ab", s2 = "eidbaooo")
    # r2 = s.checkInclusion(s1 = "ab", s2 = "eidboaoo")
    r3 = s.checkInclusion("abc", "bbbca")

   
    # print(r1)
    # print(r2)
    print(r3)

