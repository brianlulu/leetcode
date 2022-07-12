class Solution:
    def productExceptSelf(self, nums):

        # Optimal Way: TC = O(n) SC = O(1)

        # Approach:
        # we only use the result array to store the prefix and suffix 
        # iterate from start to end to store the prefix first
        # then, iterate from end to start to store the suffix

        # example: nums = [1, 2, 3, 4]
        # prefix iteration:
        # result = [1,1,1,1]; prefix = 1
        # result[0] = prefix; prefix = prefix * nums[0] => nothing before index 0 which the default prefis ix 1
            # result = [1,1,1,1] prefix = 1
        # result[1] = prefix; prefix = prefix * nums[1] => prefix before index 1 would be product of nums[0]
            # result = [1,1,1,1] prefix = 2
        # result[2] = prefix; prefix = prefix * nums[2] => prefix before index 2 would be product of nums[0]*nums[1] 
            # result = [1,1,2,1] prefix = 2 * 3 = 6
        # result[3] = prefix; prefix = prefix * nums[3] => prefix before index 3 would be product of nums[0]*nums[1]*nums[2]
            # result = [1,1,2,6] prefix = 6*4 = 24 (discard the prefix)

        # suffix iteration: 
        # result = [1,1,2,6] suffix = 1
        # result[3] = suffix * result[3](prefix @ index 3); suffix = suffix * nums[3] => nothing after index 3 which the defaul suffix is 1
            # result = [1,1,2,6] suffix = 4
        # result[2] = suffix * result[2](prefix @ index 2); suffix = suffix * nums[2] 
            # result = [1,1,8,6] suffix = 12
        # result[1] = suffix * result[1](prefix @ index 1); suffix = suffix * nums[1]
            # result = [1,12,8,6] suffix = 24
        # result[0] = suffix * result[0]; suffix = suffix * nums[0] 
            # result = [24,12,8,6] suffix = 24 (discard this)



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

