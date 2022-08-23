# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        
        # input: root -> TreeNode
        # output: root of reverse tree -> TreeNode

        # constraints:
        # # of nodes >= 0
        # Not complete binary tree

        # DFS approach:
        # iterate through the tree by dfs
        # at every iteration we just switch the child of the node
        # stop condition is that we reach the leaf

        def dfs(node):
            if not node:
                return
            
            tmp = node.left
            node.left = node.right
            node.right = tmp

            dfs(node.left)
            dfs(node.right)
        

        dfs(root)

        return root

        # TC: O(Maximum depth of the tree)
        # SC: O(1)