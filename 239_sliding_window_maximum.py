import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):

        # input: nums -> List[int], k -> int
        # output: the max number of each interation of the sliding window

        # constraints:
        # nums.length = 1
        # k >= 1
        # - <= nums <= +

        # brute forces approach
        # use sliding window and find the max for each window

        # use queue to keep track the maximum so far
        # when the window slide, we compare the new element with the top of the queue if bigger then we pop
        # if not we append
        # also we put the index inside the queue instead of the value itself to keep track the window

        result = []
        queue = collections.deque() # index
        l = r = 0

        while r < len(nums):

            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if queue[0] < l:
                queue.popleft()
            
            if (r+1) >= k:
                result.append(nums[queue[0]])
                l += 1
            r += 1


        return result

        # TC: O(N) we iterate through the nums array once and the pop is O(1)
        # SC: O(K) maximum index can be append into queue is K

if __name__ == "__main__":

    s = Solution()

    r1 = s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    r2 = s.maxSlidingWindow(nums = [1], k = 1)

    print(r1)
    print(r2)
