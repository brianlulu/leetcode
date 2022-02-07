
#input: nums: List[int], target: int
#output: List[int] (indices of two integers)

def twoSum(nums, target):

    hashMap = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in hashMap:
            return [hashMap[diff], i]
        
        hashMap[n] = i
    
    return

if __name__ == "__main__":
    result = twoSum([2,7,11,15], 9)
    result1 = twoSum([3,2,4], 6)
    result2 = twoSum([3,3], 6)

    print(result)
    print(result1)
    print(result2)

"""
Time Complexity: O(N)

    Since we use hash map to record the values and indices, 
    the average time complexity of get() and put() is O(1).
    And the worst case is that the answer are at first and last position
    which is the O(N) 

Memory Complexity: O(N)

    We use a hash map to keep track the values and indices.
    Therefore, the Memory Complexity will be O(N).

"""

