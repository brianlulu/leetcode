# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        
        # input: preorder, inorder -> List[int]
        # output: root of the tree -> TreeNode()

        # constraints:
        # len(preorder) && len(inorder) >= 1
        # len(preorder) == len(inorder)
        # the value are unique in both array
        # guarantee to have answer

        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # get the index of the preorder[0]

        # we can use mid to partition the preorder because we know that both preorder and inorder are same length
        # where finding mid of the inorder tells us that how many node on the left subtree and right subtree
        # so from the mid we know how many node to include in left subtree and right subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) 
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

    # TC: O(N^2)
    # SC: O(N^2)
    # Consider a tree that is straight line to the left, 
    # in this case preorder and inorder are reverse of each other, 
    # therefore worst case time and space complexity will both be O(N^2). 
    # Space complexity is O(N^2) because a copy of preorder and inorder 
    # with length reduced by one is created in each recursion call.


