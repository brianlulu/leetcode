class Solution:
    def threeSum(self, nums):
        
        # input = [int]
        # output = [[int]]

        res = []
        nums.sort()

        # edge case when list length is less than 3
        if len(nums) < 3:
            return res
        
        for i, num in enumerate(nums):

            # check for duplicate (i)
            if i > 0 and nums[i-1] == num:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                curSum = nums[l] + nums[r] + num

                print("l, r, num: " + str([nums[l],nums[r], num]))
                
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    
                    while nums[l+1] == nums[l] and l < r:
                        l += 1

                    l += 1
        return res


if __name__ == "__main__":

    s = Solution()
    r1 = s.threeSum([-1,0,1,2,-1,-4])

    print(r1)









