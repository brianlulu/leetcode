class Solution:
    def productExceptSelf(self, nums):

        # input = [int]
        # output = [int]

        result = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            
            if i == 0:
                result[i] = prefix
            else:
                prefix = prefix * nums[i-1]
                result[i] = prefix
            
            # print("The prefix array:" + str(result))
        
        suffix = 1

        for j in range(len(nums)-1, -1, -1):
            
            if j == len(nums)-1:
                result[j] *= suffix 
                suffix *= nums[j]
            else:
                result[j] *= suffix
                suffix *= nums[j]
                
            # print("The suffix array:" + str(result))
        
        return result

if __name__ == "__main__":

    s = Solution()
    r1 = s.productExceptSelf([1,2,3,4])
    r2 = s.productExceptSelf([-1,1,0,-3,3])

    print(r1, r2)

