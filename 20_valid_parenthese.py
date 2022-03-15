''' Question and Approach

    Input: s -> str
    Output: whether the s is a valid parentheses -> bool

    Given a string s, find out whether it is a valid parenthese

        valid parenthese:
            - it is closed with same type
                () [] {}
            - it is closed in order
                {[}] -> False
        
    Constraints:
        can we assume that () [] {} are the only symbols inside the string?
            Yes
        can s be an empty string?
            No
    
    invalid
        [
        ]
        ]]   stack: 
        [[]  
        [{]] stack: [ {]
    valid
        ()
        ()[]{}

    Stack Approach:
        1. We iterate through the string and put the opening symbol inside the stack
        2. When we have a closing symbol we pop the element in the stack and check that whether it is a correct type
            if not invalid
    
    Time Complexity: O(s.length)
    Space Complexity: O(s.length) 
        worst case: its that it is all opening brackets

    
'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hash_map = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        # close_symbol = [")", "]", "}"] 

        for c in s:
            if c in hash_map:
                stack.append(c)
            else:
                if len(stack) > 0:
                    prev_open = stack.pop()
                    if hash_map[prev_open] != c:
                        return False
                else: # no opening brackets but have close brackets now
                    return False
        
        return True if len(stack) == 0 else False

'''
edge case:
    s = [; stack = [ "[" ] False
    s = }; stack = [  ]
    s = [{]}; stack = [ "[", "{", ]
    s = ([]); stack = [ ]
'''