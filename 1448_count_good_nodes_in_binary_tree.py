# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        
        # input: root -> TreeNode
        # output: total number of the "good" node -> int

        # "good" node X -> from root to X, the nodes in between are not greater than X
        
        # constraints:
        # root >= 1
        # TreeNode.val is not unique and is always numerical

        # DFS pre-order recursive approach:
        # use a curMax variable to keep track the maximum value we have seen in this path
        # if the curNode >= curMax -> good node += 1
        # if not continue
        
        self.result = 0

        def dfs(node, curMax):
            if not node:
                return
            # check good node and update curMax
            if node.val >= curMax:
                self.result += 1
                curMax = node.val
            
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        dfs(root, root.val)

        return self.result

        # TC: O(N) -> N is the total number of nodes in tree
        # SC: O(H) 