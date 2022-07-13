class Solution:
    def isPalindrome(self, s: str) -> bool:

        # input: str
        # output: boolean -> whether the s is palidrome or not

        # constraints:
        # s consists only ASCII 
        # 1 <= s.length <= 2*10^5 

        # Two Pointer Approach:
        # we first check that whether the current element is a alphanumeric or not
        # convert to lowercase, if needed
        # compare the L R pointer elements are the same or not
        # the stop condition is that when L == R or L > R

        l, r = 0, len(s) - 1
        

        
        while l < r:
            # check alphanumirc; convert to lowercase (USE ASCII)
            while not self.isAlphaNum(s[l]) and l < r:
                l += 1
            
            while not self.isAlphaNum(s[r]) and r > l:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNum(self, c):
            return (ord("A") <= ord(c) <= ord("Z") or 
            ord("a") <= ord(c) <= ord("z") or 
            ord("0") <= ord(c) <= ord("9"))


if __name__ == "__main__":

    s = Solution()
    r1 = s.isPalindrome(s = "A man, a plan, a canal: Panama")
    r2 = s.isPalindrome(s = "race a car")

    print(r1)
    print(r2)