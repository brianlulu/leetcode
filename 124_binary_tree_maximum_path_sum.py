# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math


class Solution:

    def maxPathSum(self, root) -> int:
        
        # input: root -> TreeNode 
        # output: maximum path sum of the tree -> int

        # path is that for two adjacent node is connected by an edge

        # constraints:
        # tree # >= 1
        # node.val is always numerical
        # cannot reuse a node, meaning node can exist in the path once

        # DFS recursive approach:
        # bottom up and ask its left child and right child that their maximum path sum
        # 1. when returning the maximum path sum we have to return the path not the subtree sum
        # 2. keep updating the global maximum
        # 3. recursive function call stop condition -> when reach to the leaf

        self.result = root.val

        def dfs(root):

            if not root:
                return 0

            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right),0)

            curMax = max(leftMax + rightMax + root.val, root.val + leftMax, root.val + rightMax)
            
            self.result = max(self.result, curMax)

            return max(root.val + leftMax, root.val + rightMax)

        dfs(root)

        return self.result

        #TC: O(N)
        # SC: O(H)