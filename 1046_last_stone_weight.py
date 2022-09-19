import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        
        # input: stones -> list[int]; stones[i] is the weight of the stones
        # output: the weight of the remaining stone -> int

        # constraints:
        # at the end, at most one stone is left
        # if no stone left, return 0
        # 1 <= stones.length <= 30
        # 1 <= stones <= 1000 

        # MaxHeap Approach:
        # use a while loop and keep removing elements until the size of max heap <= 1 
        
        maxHeap = [-1*s for s in stones]
        print(maxHeap)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            firstStone = heapq.heappop(maxHeap) * -1
            secondStone = heapq.heappop(maxHeap) * -1
            if firstStone - secondStone > 0:
                heapq.heappush(maxHeap, -(firstStone - secondStone))
        
        return -maxHeap[0] if maxHeap else 0
        

        # TC: O(NLogN)
        # SC: O(N)