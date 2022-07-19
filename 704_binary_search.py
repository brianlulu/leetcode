class Solution:
    def search(self, nums, target):
        
        # input: nums -> List[int]; target -> int
        # outpu: index of the target inside the nums array

        # constraints:
        # nums.length >= 1
        # all numbers in nums are unique
        # nums can have negative and positive

        # binary search:
        # use left right mid pointers to find the target
        # mid = (right + left) // 2 or mid = (right - left) // 2 + left
        # if mid > target, shift right pointer to mid - 1
        # else (mid < target) shift left pointer to mid + 1
        # if mid == target, return index

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            
        return -1

        # TC: O(logN)
        # SC: O(1)

    
if __name__ == "__main__":

    s = Solution()

    r1 = s.search(nums = [-1,0,3,5,9,12], target = 9)
    r2 = s.search(nums = [-1,0,3,5,9,12], target = 2)

    print(r1, r2)