# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        
        ''' --- DFS Recursive ---
        self.result = 0
        
        def dfs(node, depth):
            
            if not node:
                self.result = max(depth, self.result)
                return
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        return self.result
        
        '''

        ''' --- NeetCode Method ---

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        '''

        ''' --- BFS (Queue) ---
        
        level = 0
        queue = deque([root])

        if not root:
            return 0

        while queue:
            currQueueLength = len(queue)
            for i in range(currQueueLength):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return level
        '''

        # iterative DFS (Stack)
        if not root:
            return 0

        stack = [(root, 1)]
        result = 1

        while stack:
            node, depth = stack.pop()
            result = max(depth, result)

            if node.right:
                stack.append((node.right, depth + 1))
            
            if node.left:
                stack.append((node.left, depth + 1))
            
        
        return result

