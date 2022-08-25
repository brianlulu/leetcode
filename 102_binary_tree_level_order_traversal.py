# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root):
        # input: root -> TreeNode
        # output: level order traversal -> List[List[int]]

        # constraints:
        # tree can be empty
        # every node.val is numerical

        # BFS approach
        # use queue to implement
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            curLevelCount = len(queue)
            curLevel = []
            for i in range(curLevelCount):
                node = queue.popleft()
                curLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(curLevel)

        return result

        # TC: O(N)
        # SC: O(N) N = 2^H 2^H - 2^(H-1) = 2^(H-1) = N/2