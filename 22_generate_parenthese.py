class Solution:
    def generateParenthesis(self, n: int):
        
        # input: n -> int
        # output: all combinations of parentheses given n pair of them -> List[str]

        # constraints:
        # n >= 1
        # the order of the output dont matter

        # brute force approach:
        # generate all possible combinations of n pair parentheses
        # check which combinations is a well-formed one
        # TC(2^n) to generate all possible combination of parentheses
        # SC(2^n) use for storing every possible combination of parenthese

        # backtracking approach (function stack):
        # there shouldnt have a close parenthese that is generate before having a open parenthese
        # base case = open == n and close == n
        # from this, we can construct a condition:
            # when generating the results the close parenthese can only be added to result
            # if # of close < # of open
            # the open parenthese can only be added if the # of open < n
        # n = 2, open = 0, close = 0
        # tmp = (, open = 1, close = 0
        # tmp = (), open = 1, close = 1; tmp = ((, open = 2, close = 0
        # tmp = ()( open = 2, close = 1 ; tmp = (() open = 2, close = 1
        # tmp = ()() open = 2, close = 2 ; tmp = (()), open = 2, close = 2

        result = [] # use for append all the well-formed parenthese

        def backTrack(curr = "", open = 0, close = 0):
            
            # base case
            if open == n and close == n:
                result.append(curr)
                return

            # backtracking function call by conditions
            if open < n:
                backTrack(curr + "(", open + 1, close)
            if open > close:
                backTrack(curr + ")", open, close + 1)
            
            return
        
        backTrack()

        return result

        # TC:O(2N) -> O(N)
        # SC:O(2N) -> O(N)
        
        
if __name__ == "__main__":

    s = Solution()
    r1 = s.generateParenthesis(n = 1)
    r2 = s.generateParenthesis(n = 2)
    r3 = s.generateParenthesis(n = 3)

    print(r1)
    print(r2)
    print(r3)


        
            

            
