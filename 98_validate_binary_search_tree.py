# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from math import inf


class Solution:
    def isValidBST(self, root):
        
        # input: root -> TreeNode
        # output: whether the input tree is a valid BST -> bool

        # valid BST -> the right subtree of a node is always less than its children, 
        # whereas, the left subtree of a node is always greater than its children

        # constraints:
        # N >= 1
        # abs(node.va) >= 2^31 - 1 

        # DFS approach:
        # use recursive method to implement
        # use a left boundary and right boundary to keep track the valid BST condition
        #   when go left child, update right bound
        #       go right child, update left bound

        def dfs(node, leftBound, rightBound):
            if not node:
                return True
            
            if leftBound >= node.val or rightBound <= node.val:
                return False

            return dfs(node.left, leftBound, node.val) and dfs(node.right, node.val, rightBound)

        return dfs(root, -inf, inf)

        # TC: O(N)
        # SC: O(H)