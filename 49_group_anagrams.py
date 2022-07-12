class Solution:
    def groupAnagrams(self, strs):

        # input: List[str]
        # output: List[List[str]]

        # constraints: 
        # 1 <= strs.length <= 10^4
        # all lower case letters
        # 0 <= strs[i].lengths <= 0

        # use hashmap to keep track what anagram we have
        # { anagram type : [original strings] } return the values of the hashmap as result
        # [a..z] "eat" = [1,0,0,0,1, .. 1, 0,0 ..]

        anagram = {}

        for s in strs:
            countLetters = [0] * 26

            for l in s:
                countLetters[ord(l) - ord("a")] += 1 # shift the acis value to 0 which is letter "a"

            if tuple(countLetters) in anagram:
                anagram[tuple(countLetters)].append(s) # the python dictionary type cannot take list as key 
                                                       # since it is mutable
            else:
                anagram[tuple(countLetters)] = [s]

        
        return anagram.values()

if __name__ == "__main__":

    s = Solution()
    r1 = s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
    r2 = s.groupAnagrams(strs = [""])

    print(r1)
    print(r2)

