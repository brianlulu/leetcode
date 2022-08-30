# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):

        # input: root -> TreeNode; k -> int
        # output: kth value -> int

        # constraints:
        # node # >= k >= 1
        
        # DFS iterative in-order traversal approach:
        # traverse through the tree in-order. In this way, we can construct a sorted array
        # use stack tto implement
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            
            curr = curr.right

    # TC: O(H) worst case find the kth = n value and the tree is a linked list
    # SC: O(H) 

