import heapq

class KthLargest:

    # constraints:
    # guaranteed that there is always at k elements
    # 1 <= k <= 10^4
    # 0 <= nums.length <= 10^4
    # -10^4 <= val <= 10^4, no overflow 
    
    # MaxHeap approach (Brute Force):
    # heapify the nums and to find kth for add
    # we pop kth time and then we add back the element we popped
    # TC: O(2k * logN) -> O(klogN)
    # SC: O(N-K)

    # MinHeap with Size K approach:
    # Since we finding the Kth Largest, this means that if we use a min heap with size k
    # we can always have the Kth largest at root

    def __init__(self, k, nums):

        # input: k -> int, nums -> List[int]        
        # output: None but create a KthLargest object with the appropriate data structure
        
        self.k = k
        self.minHeap = nums 
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:

        # input: val -> int
        # output: the kth largest after adding -> int

        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)