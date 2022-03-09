class Solution:
    def longestConsecutive(self, nums):
        
        # input: nums -> List[int]
        # output: the length of longest consecutive sequences -> int

        # convert the nums into hashset
        hash_set = set(nums)
        result = 0

        # iterate through nums
        for n in nums:
            # check start of sequence
            if (n-1) not in hash_set:
                length = 1
                cur = n
            # check the next element of sequence if its there add to length of current sequence
                while cur+1 in hash_set:
                    length += 1
                    cur += 1
            # compare with result
                result = max(result, length)
        
        return result

    ''' 
    Test Case: [0,3,7,2,5,8,4,6,0,1]

    n = 0, 
        length = 1, cur = 0
        length = 2, cur = 1
        length = 3, cur = 2
            ...
        length = 9, cur = 8

        result = 9
    
    n = 3
    n = 7
        ...

    n = 0
        result = 9

    Test Case = []
    
    result = 0
    '''

    '''
    Time Complexity: O(n) because we do not try to build every sub consecutive sequence for every element instead 
        we just build sequence from the start of the consecutive sequence
    
    Space Complexity: O(n) we use hashset
    '''


if __name__ == "__main__":

    s = Solution()
    r1 = s.longestConsecutive([100,4,200,1,3,2])
    r2 = s.longestConsecutive([0])
    r3 = s.longestConsecutive([])

    print(r1)
    print(r2)
    print(r3)