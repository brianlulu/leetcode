class Solution:
    def search(self, nums, target: int) -> int:
        
        # input: nums -> List[int] target -> int
        # output: index of target or -1 if target not in nums -> int
        
        # constraints:
        # nums >= 1
        # in ascending order, possibily rotated
        # all uniqle value

        # binary search approach:
        # modify the original binary search 
        # when using binary search, we are bascially just cutting half of our searching range
        # since the array is rotated but still we know that some part of the array is in ascending order
        # then we can use this property to modify our binary search
        # first identify which part of array is sorted
        # if mid > l -> left part is sorted
            # if target > mid of target < l -> shift l = mid + 1
            # else shift r
        # if mid < r -> right part is sorted
            # if target > r or target < mid shift r = mid - 1
            # else shift l


        
        l, r = 0 , len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            
            # left sorted part
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted part
            elif nums[mid] <= nums[r]:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        
        return -1

        # TC: O(logN)
        # SC: O(1)


if __name__ == "__main__":

    s = Solution()

    r1 = s.search(nums = [4,5,6,7,0,1,2], target = 0)
    r2 = s.search(nums = [4,5,6,7,0,1,2], target = 3)

    print(r1)
    print(r2)

