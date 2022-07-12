class Solution:
    def topKFrequent(self, nums, k):

        # inputs: [int] nums, int k
        # outputs: [int] which represent the top k most freqent elements in nums
        

        # heap approach:
        # we can use max heap to store the counts of the elements
        # time complexity would be k*log(n) where if the k = n, then it would be n*logn
        # the log(n) is the time complexity for creating a heap

        # bucket sort approach:
        # we can use bucket sort with the frequency as the index.
        # in this way, the maximum data structure (array) for storing the bucket sort algorithm is n (the input size of nums)
        # time complexity would be O(2n) -> O(n)
        # one O(n) would be using hashmap to keep the counts
        # one O(n) would be iterate through the array k times, worst case k = n
        # space complexity would be O(n)
        # the bucket list and the count hashmap

        count = {}  # keep track the frequency of the elements { num : frequency }
        bucket = [[] for i in range(len(nums)+1)]
        result = []

        for n in nums:
            count[n] = 1 + count.get(n, 0) # this handle the edge case when there is no element in the hashmap

        for n, c in count.items():
            bucket[c].append(n)

        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
        

if __name__ == "__main__":

    s = Solution()

    r1 = s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
    r2 = s.topKFrequent(nums = [1], k = 1)

    print(r1)
    print(r2) 
