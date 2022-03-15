'''
    input: s -> str
    output: whether the string s still a palindrom if deleting one character from string -> bool
    
    Given a string s, check whether the string is still palindrom after removing one character from it
    
    Constraints:
        can it be empty string?
            No
        is there upper case in s?
            No, only lowercase
    
    Brute Force Approach:
    
        iterate through the string and remove current index character and check the remaining string are palindrom or not
        
        Method to check palindrom:
            aba
        
        O(N^2) 
        
    Two Pointer Approach:
        - odd length
            aba
            a
        - even length
            aa
            baab
        we first check that the string s is odd or even
        Then use two pointer starting from the middle index and recreate the string while checking that whether the substring is palindrom
          l       r
        a c c a c b a
        a c a d c a or a b c a a    
         
        abba
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1
        removal_char = False
            
        while l < r:
            
            if s[l] != s[r]:
                return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
            else:
                l += 1
                r -= 1

        return True
    
''' Test Case

"aba"

'''
        
        
        
        
        
        
        
        
        
        
        
        