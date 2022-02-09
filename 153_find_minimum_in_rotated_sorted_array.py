class Solution:
    def findMin(self, nums):

        #input = [int]
        #output = int

        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:

            # first compare if right > left we know that mid > left
            # so check result with left
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            
            
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            
        return res


if __name__ == "__main__":

    s = Solution()
    r1 = s.findMin([3,4,5,1,2])
    r2 = s.findMin([4,5,6,7,0,1,2])
    r3 = s.findMin([11,13,15,17])

    print(r1, r2, r3)



