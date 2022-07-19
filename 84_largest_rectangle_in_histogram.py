class Solution:
    def largestRectangleArea(self, heights) -> int:
        
        # input: heights -> List[int]
        # output: the largest rectangle in the histogram -> int

        # constraints:
        # heights.length > 0
        # each histagram is always 1 unit width
        # heights > 0

        # Stack approach:
        # we calculate the current possible largest rectangle we can construct
        # use a stack to keep track the index and height of the rectangle
        # the element inside the stack (index, heights). This means that
        # from index to current index we still can construct rectangle with 
        # (current index - past index) with the height. The stack should be in 
        # non-strictly increasing order because if the current index height is smaller
        # than the top element of the stack. Then rectangle can not be extended to the right


        stack = [] # keep track the possible rectangle to construct (height, index)
        result = 0 # to keep track the largest rectangle
        
        for i in range(len(heights)):
            currHeight = heights[i]
            if not stack:
               stack.append((currHeight, i))
               continue

            if currHeight >= stack[-1][0]:
                print(stack)
                stack.append((currHeight, i))
            else:
                while stack and currHeight < stack[-1][0]:
                    prev = stack.pop()
                    rectangle = (i - prev[1]) * prev[0]
                    result = max(rectangle, result)
                stack.append((currHeight, prev[1]))
            
        while stack:
            prevH, prevI = stack.pop()
            result = max(prevH * (len(heights)-prevI), result)
        
        return result

        # TC: O(N)
        # SC: O(N)


if __name__ == "__main__":

    s = Solution()

    r1 = s.largestRectangleArea(heights = [2,1,5,6,2,3])
    r2 = s.largestRectangleArea(heights = [2,4])

    print(r1)
    print(r2)



