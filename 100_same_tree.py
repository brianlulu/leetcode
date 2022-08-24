# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSameTree(self, p, q) -> bool:
        
        # input: p, q -> TreeNode
        # output: whether both tree are the same -> bool

        # same tree = the tree structure is the same. the value inside each node at each position is the same

        # constraints:
        #   node # in tree >= 0
        #   node.val is numerical


        # BFS approach:
        # use two queue to keep track both tree
        # compare the value of the node 
        #   if same put left child and right child
        #   else return false
        # have to check the remaining of the queue 

        queue = deque([p, q])

        while queue:
            nodeP, nodeQ = queue.popleft()

            if not self.check(nodeP, nodeQ):
                return False

            # we only need to check for p because when use check() the two cases that are True are:
            # 1. nodeP and nodeQ are both None
            # 2. nodeP and nodeQ are both not None and They are same node
            # so at the part we only use p because we just need to check that nodeP is not None
            # if nodeP is not None then this imply nodeQ is not None  
            if nodeP:  
                queue.append((nodeP.left, nodeQ.left))
                queue.append((nodeP.right, nodeQ.right))
            
        
        return True

    def check(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        return True
    
    # TC: O(N)
    # SC: O(2^(H-1) = N/2) = O(N) (2^H) = N worst case: the full binary tree