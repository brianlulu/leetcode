import heapq


class Solution:
    def kClosest(self, points, k):
        
        # input: points -> [[int]], k -> int
        # output: kth closest point to origin -> [[int]]

        # constraints
        # points >= k >= 1
        # -10^4 < x, y < 10^4

        # min heap approach
        # (euclidean distance, coordinate)
        # go through the points list one by one and calculate the euclidean distance
        # then push the tuple into min heap
        # then pop k th element

        min_heap = []
        result = []

        heapq.heapify(min_heap)

        for p in points:
            distance = (abs(p[0])**2) + (abs(p[1])**2)
            heapq.heappush(min_heap, (distance, p))    
            
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])

        
        return result
        # TC: O(N * LogN) + O(K*LogN) -> O(2NLogN) -> O(NLogN)
        # SC: O(N)

