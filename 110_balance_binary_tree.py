# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        
        # input: root -> TreeNode
        # output: whether this tree is height-balance -> bool

        # constraints
        # tree node # >= 0

        # DFS approach:
        # use recursive and calculate the height of each node
        # if the height difference between two subtree is larger than 1 
        # then return false

        def dfs(node):
            if not node:
                return (True, 0)
            
            balancedLeft, heightLeft = dfs(node.left)
            balancedRight, heightRight = dfs(node.right)


            if abs(heightLeft - heightRight) > 1 or not balancedLeft or not balancedRight:
                return (False, 1+max(heightLeft, heightRight))
            
            return (True, 1+max(heightLeft, heightRight))
        
        return dfs(root)[0]


    # TC: O(N)
    # SC: O(1)