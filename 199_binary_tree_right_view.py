# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):

        # input: root -> TreeNode
        # output: values of node from right side(top to bottom) -> List[int]

        # constraints:
        # root >= 0
        # treeNode.val all numerical

        # BFS approach:
        # use queue to implement the BFS
        # at each iteration, keep track the length of the queue as the node counts for each level
        # append the node value for the first pop node
        # append the not null child into the queue (right child first)

        result = []
        
        if not root:
            return result

        queue = deque([root])

        while queue:
            currLevelLength = len(queue)

            for i in range(currLevelLength):
                curNode = queue.popleft()
                if i == 0:
                    result.append(curNode.val)
                
                if curNode.right:
                    queue.append(curNode.right)
                if curNode.left:
                    queue.append(curNode.left)

        return result

        # TC: O(N) N is the total number of node 
        # SC: O(N) 

