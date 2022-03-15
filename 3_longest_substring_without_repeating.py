''' Question And Thinking Process
Input: s -> str
Output: length of longest substring without repeating -> int

Given a string s find the length of longest substring without repeating

Constraints: 
    0 <= s.length <= big num (Empty String)
        edge case: s = ""
    s contains digit characters symbol

Brute Force Approach:
    - Find all the substring from every index
        1. Iterate through every character and compose the substring (Repeat Work)
        2. Then calculate the length of valid substring
        3. use a variable result to keep track the largest length every iteration

    Time Complexity: O(n^2)
    Space Complexity: O(1)

Sliding Window (2 pointer approach):
    - Use a left pointer and a right pointer to compose the valid substring

        use left pointer and right pointer to traverse through list
            if s[r] in set:
                remove s[r] in set
                add s[r]
                update l
        every iteration we update result
    
    a b c a b [c, a, b]   <- (set)  
        l   
            r
    
    Time complexity: O(n)
    Space Complexity: O(n)

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        
        substring = set()
        l = 0
        result = 0

        for r in range(0, len(s)): # edge case s = ""
            
            if s[r] in substring:
                while s[r] in substring:
                    substring.remove(s[l]) 
                    l += 1
                
            substring.add(s[r])
            
            result = max(result, len(substring))
    
        return result


    '''
    s = "bbb" result = 1

        substring = set(b)
        l = 2
        result = 1

        r = 0, s[0] = b, 
        r = 1, s[1] = b 
        r = 2, s[2] = b

        
    edge case: s = ""
        substring = set()
        l = 0
        result = 0

    s = "bbb" result = 1
        
        substring = set()
        l = 1
        result = 1

        r = 0
        r = 1
    '''