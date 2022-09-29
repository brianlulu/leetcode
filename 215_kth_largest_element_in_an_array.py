import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # input: nums -> List[int], k -> int
        # output: kth largest element -> int
        
        # When there is a duplicate element in num, kth largest != kth distinct largest
        # Ex [4,4,4,3,2] k = 3; Output -> 4

        # constraints
        # nums >= k >= 1
        
        # min heap approach
        # use a len(k) min heap data structure
        # iterate through nums
        #   when the number is larger than the smallest element in min heap OR
        #   when len(minheap) < k
        #       we add element into the minheap
        ''' Min Heap
        min_heap = nums[0:k]
        heapq.heapify(min_heap)

        for n in nums[k:]:
            cur_min = heapq.heappop(min_heap)
            if cur_min < n:
                heapq.heappush(min_heap, n)
            else:
                heapq.heappush(min_heap, cur_min)
        
        return heapq.heappop(min_heap)

        '''

        
         
        