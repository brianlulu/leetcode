# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        #input: root -> TreeNode
        #output: the longest length between two node (edges counts) -> int

        # constraints:
        # node # >= 1
        
        # DFS Approach
        # calculate the diameter at current node
        # return the max(left.child.diameter, right.child.diameter)

        self.result = 0

        def dfs(node):
            if not node:
                return 0
            
            maxLeft, maxRight = dfs(node.left), dfs(node.right)
            
            self.result = max(self.result, maxLeft + maxRight)

            return 1 + max(maxLeft, maxRight)

        dfs(root)

        return self.result

    #TC: O(N)
    #SC: O(1)

