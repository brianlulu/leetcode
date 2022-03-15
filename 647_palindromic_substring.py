''' Question And Approach

    Input: s -> str
    Output: numbers of substring that are palindrom -> int

    Given a string s, calculate how many substring is palindrom

    palindrom condition:
        read from start is the same as reading from the backward direction

        "a", "aa", "bccb"
    
    substring:
        contiguous sequence
    
    Constraints:
        is s empty string? 
            No
        is there capital letters in s?
            No, all lower case
'''

'''    Brute Force Approach:
    
    Create all the substring and calculate how many substrings are palindrom
    abc
    a; ab; abc
    b; bc
    c

    O(n^2) 
    O(m)

    Middle Index Substring Approach:

    " a a a c"
      l
      r    
'''

''' Center Approach:

    Using 2 pointer generate the substring by choosing the current character as the center of the palindrom.
        if the next substring created is not palindrom, we can iterate to next character
        if the next substring created is a palindrom, we expand the substring until it is not.

      a b
      l
      r
        
        1 -> 3 -> 5

    Time complexity: O(N * N/2) + O(N* N/2) => O(2N^2) => O(N^2)
    Space Complexity: O(1)

'''
class Solution:
    def countSubstrings(self, s: str) -> int:

        # odd center
        result = 0
        increment_boundary = (len(s) // 2) + 1
        for i in range(len(s)):    
            l = r = i
            result += 1

            for j in range(1, increment_boundary):
                if (l - j < 0 or r + j >= len(s)): # out of bound
                    break
                if s[l - j] == s[r + j]:
                    print(s[l - j:r + j + 1])
                    result += 1
                else:
                    break
            
        # even center
        for i in range(len(s)):    
            l = i
            r = i + 1
            if r < len(s):
                if s[l] == s[r]:
                    result += 1
                    for j in range(1, increment_boundary):
                        if (l - j < 0 or r + j >= len(s)): # out of bound
                            break
                        if s[l - j] == s[r + j]:
                            print(s[l - j:r + j + 1])

                            result += 1
                        else:
                            break

        return result
        
        # substring = []
        # l = 0

        # # create all substrings
        # while l < len(s):
        #     for r in range(1,len(s)+1):
        #         if s[l:r]:
        #             substring.append(s[l:r])
            
        #     l += 1

        # result = 0
        # # check substring are palindrom
        # for string in substring:
        #     new_string = ""

        #     for s in string:
        #         new_string = s + new_string
            
        #     if new_string == string:
        #         result += 1
        
        # print(substring)
        
        # return result

''' Test Case

s = "a", substring = ["a"]

copy = a
new_string = ""

s = "ab" substring = [a, ab, b]





'''
    
if __name__ == "__main__":
    
    s = Solution()

    r1 = s.countSubstrings("xkjkqlajprjwefilxgpdpebieswu")
    r2 = s.countSubstrings("abc")

    print(len("xkjkqlajprjwefilxgpdpebieswu"))
    print(r1, r2)

        




        
        
        