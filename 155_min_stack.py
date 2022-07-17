class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.curMin = value
    
    def setCurMin(self, val):
        self.curMin = val

        
class MinStack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val: int) -> None:
        node = Node(val)

        if self.head:
            if node.curMin > self.head.curMin:
                node.setCurMin(self.head.curMin)
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.value       

    def getMin(self) -> int:
        return self.head.curMin
        

# input: function calls and argument
# output: output of functions

# stack implementation:
# we can use a link list to construct the stack
# use a top variable/pointer to keep track the top of the stack

# to achieve link list structure we should also construct a node class
# inside the node class
# use a value variable to keep track the value
# use a next variable/pointer to point to the next node
# use a curMin value to keep track the current min at the node
# in this way we can also have the minimum at each node inside the stack

# two stack implementation
# we use list to construct both stacks 
# we use one stack to keep track the original stack
# use the second stack to keep track the minimum so far
# Example
# stack =     [1,2,-1,3]
# minstack  = [1,1,-1,-1]

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []
    
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if self.minStack:
#             self.minStack.append(min(val, self.minStack[-1]))
#         else:
#             self.minStack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()
    
#     def top(self) -> int:
#         return self.stack[-1]
    
#     def getMin(self) -> int:
#         return self.minStack[-1]

