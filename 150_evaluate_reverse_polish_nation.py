class Solution:
    def evalRPN(self, tokens) -> int:
        
        # input: tokens -> List[str]
        # output: RPN result -> int
        
        # constraints:
        # tokens.length >= 1
        # tokens only contains operand and digits
        # guaranted result from all input
        # floor division
        
        # stack approach:
        # use stack to keep track the numbers 
        # iterate through element in tokens
        # if operand, 
        #   pop 2 element from stack
        #   do the math operation
        #   push back to stack
        # if number,
        #   push into stack

        stack = []

        for c in tokens:
            if c in ['+', '-', '*', '/']:
                first = stack.pop()
                second = stack.pop()
                if c == '+':
                    stack.append(first + second)
                elif c == '-':
                    stack.append(second - first)
                elif c == '*':
                    stack.append(first * second)
                else:
                    # the trick is here in python turcate toward 0, when use floor the positive value will 
                    # perform correctly. However, if negative, the floor division actually will round down
                    # meaning "turcate away from 0" (-1.5 -> -2) but the problem ask us to turcate toward 0!
                    # so we cannot use "//" or "floor()". In general, other programming language such as Java
                    # and c++ turcate toward 0
                    stack.append(int(second/first)) 

            else:
                stack.append(int(c))
                
        return stack[-1]

        # TC: O(n) just iterate through the whole list once
        # SC: O(n) even though we do not append the operand into stack but we can estimate that 3 element to 
        # create an math operation (2 nums and 1 operand). Therefore, worst case O(2N/3) -> O(N)

