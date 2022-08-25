# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        
        #input: root -> TreeNode subRoot -> TreeNode
        #output: whether the subRoot is a subtree of the root -> bool

        # sub tree condition:
        # 1. same structure
        # 2. same node.val
        # 3. same number of nodes, meaning if the a subtree in root tree has one more node than 
        #       the subRoot tree, then it is NOT a subtree even tho the root subtree contains all
        #       of the nodes in subTree.

        # constraints
        # node # for root and subRoot >= 1


        # Approach
        # 1. implement a helper function for checking its the same tree or not
        # 2. use DFS to traverse the tree
        # 3. compare the node.val with subRoot.val
        #       if same, call helper function
        #       else, keep traverse
        if not subRoot:
            return True
        # after the above if condition we know that subRoot is not null
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, treeNode, subNode):
        if not treeNode and not subNode:
            return True

        if not treeNode or not subNode:
            return False

        if treeNode.val == subNode.val:
            return self.sameTree(treeNode.left, subNode.left) and self.sameTree(treeNode.right, subNode.right)

        return False


    
    # TC: O(R * S) R is node # of the root tree and S is the node in subtree
    # SC: O(R*S)