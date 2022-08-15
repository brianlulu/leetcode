class Solution:
    def findDuplicate(self, nums) -> int:
        
        # input: nums -> List[int]
        # output: the duplicate number in the list -> int

        # constraints:
        # guarantee only one integer that is duplicate
        # len(nums) = n + 1
        # 1 <= nums[i] <= n

        # Floyd's cycle detection approach:
        # 1. identify the problem is a link list problem
        #   since we know that 1 <= nums[i] <= n and len(nums) = n + 1,
        #   we can say that the value, nums[i], be the index of the nums. 
        #   This will create a cycle linked list because there is duplicate 
        #   value inside the list. Also, since 1 <= nums[i] <= n, we guarantee that
        #   the we dont link any index out-of-bound
        #   Ex.  nums = [1,3,4,2,2] len(nums) = 4 + 1
        #   Then nums[0] -> nums[1] -> nums[3] -> nums[2] -> nums[4] -> nums[2]
        #   
        # 2. use fast and slow pointer to detect the intersection node
        #   the intersection node != the cycle start point.
        # 3. use slow2 pointer which start at head and traverse 1 node each iteration
        #   with slow pointer doing the same thing (traverse 1 node each iteration)
        #   when slow == slow2 then thats the cycle start point which is the duplicate number
        #   This is proved by Floyd's cycle detection
        # Floyd's cycle detection:
        # Let p = distance between head and cycle start; c = cycle start
        # let x = distance between cycle start and intersection of the slow and fast pointer
        # we know that 2 slow = fast (fast traverse 2 node a time while slow traverse 1 node at a time)
        # 2 * (p + c - x) = p + 2c - x (the intersection point)
        # 2p + 2c - 2x = p + 2c - x -> p = x (this proves the step 3)
        
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        
        # TC: O(C*N) -> O(N)
        # SC: O(1)
        