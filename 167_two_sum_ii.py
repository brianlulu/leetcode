class Solution:
    def twoSum(self, numbers, target):
        
        # NOTE: the array in this problem is 1-indexed!!!
        # input: numbers -> List[int]; target -> int
        # output: List[int] -> two indices of elements of the target sum
        
        # constraints:
        # guarrented one solution
        # can only use one element once
        # 2 <= numbers.length <= 3*10^4
        # sorted in non-decreasing order

        # Brute force approach:
        # use two for loop
        # iterate through every elements in the array
        # for each element we iterate from the current element to the end of the array
        # we can stop iterate if the sum of the element is bigger than the target

        # Two pointer approach:
        # use two pointer to calculate the current sum and compare with the target
        # if current sum is smaller than the target, shift the left pointer
        # if the current sum is bigger than the target, shift the right pointer
        # we can do this because the array is sorted in non-decreasing order
        # after we find the solution, we added one to the left right pointer since an 1-indexed array is given 

        l, r = 0, len(numbers)-1
        curr = numbers[l] + numbers[r]

        while curr != target:
            if curr < target:
                l += 1
            if curr > target:
                r -= 1
            curr = numbers[l] + numbers[r]

        return [l+1, r+1]

        # TC: O(N)
        # SC: O(1)


if __name__ == "__main__":

    s = Solution()
    
    r1 = s.twoSum(numbers = [2,7,11,15], target = 9)
    r2 = s.twoSum(numbers = [2,3,4], target = 6)

    print(r1)
    print(r2)