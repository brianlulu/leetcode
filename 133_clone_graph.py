# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        
        # input: node (adjList) -> [[int]]
        # output: deep copy (adjList) -> [[int]]

        hashMap = {}

        def dfs(node):

            if node in hashMap:
                return hashMap[node]
            
            copy = Node(node.val)
            hashMap[node] = copy
            
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node) if node else []

    '''
        Time complexity: O(N) where N = Edges + Vertices because we traverse through every vertices and clone them. 
            Also, we traverse through edges 
        Space Complexity: O(V) we use the hashMap to store the vertices

    '''
