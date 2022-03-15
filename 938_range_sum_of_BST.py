# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

''' Questions and Approach
    Input: root -> TreeNode, low -> int, high -> int
    Output: sum of the node value in between low and high (inclusive)
    
    Given a Binary Search Tree root TreeNode, return the sum value of any low <= TreeNode.val <= high
    
    Constraints:
        node.val > node.left.val and node.val < node.right.val => the node value are all uniqle
        low high and val are all int? thats why we return int
        
        is there emtpy tree?
            No
            
    Brute Force Approach:
        DFS traverse through every tree node and sum up the value that is in between low and high
        
    Time Complexity: O(N) where N is the node number
    Space Complexity: O(N) if the binary is not balance (the worst is that a linear tree (singly linked list))
            O(logN) => O(height of Tree)
'''

class Solution:

    def rangeSumBST(self, root, low, high):
        
        
#         def dfs(node):
#             if not node:
#                 return 

#             if node.val >= low and node.val <= high:
#                 self.result += node.val
            
#             if node.val <= low:
#                 dfs(node.right)
#             elif node.val >= high:
#                 dfs(node.left)
#             else:
#                 dfs(node.left)
#                 dfs(node.right)

#         self.result = 0
#         dfs(root)
#         return self.result

        queue = deque()
        queue.append(root)
        result = 0
        while queue:
            currNode = queue.popleft()
            if currNode:
                if low <= currNode.val <= high:
                    result += currNode.val

                if currNode.val <= low:
                    queue.append(currNode.right)
                elif currNode.val >= high:
                    queue.append(currNode.left)
                else:
                    queue.append(currNode.left)
                    queue.append(currNode.right)
            
        return result
        
'''
    10
    /\
   5  15
  /\    \
 3 7     18
 
 
 low = 7, high = 15
 result = 32

 
 
 
'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        