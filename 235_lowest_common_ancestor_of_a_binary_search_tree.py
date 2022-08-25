# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # input: root, p, q -> TreeNode
        # ouput: lowest common ancestor (LCA) of p and q -> TreeNode

        # LCA is the node that contains p and q as its descendants. Also the node can be a descendants of itself
        # meaning, if p contains q as its descendants, the p is the LCA

        # constraints:
        # root >= 2 -> p and q are not null
        # all node.val are unique
        # p != q
        # p and q exist in root
        # root is a binary search tree

        # Binary search method:
        # since it is a binary search tree, we can use the characteristic of the leftChild < Node < rightChild
        # LCA is going to be the node that split p and q into two subtree, meaning (p or q) < LCA < (the left over)
        # OR LCA is p or q itself 
        
        curr = root

        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr

        # TC: O(logN)
        # SC: O(1)
        
        