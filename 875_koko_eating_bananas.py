from math import ceil


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        
        # input: piles -> List[int]; h -> int
        # output: minimum banana eating speed k to finish every pile in h -> int

        # constraints: 
        # 1 <= piles.length <= h
        # piles[i] >= 1

        # brute force approach:
        # try every k starting from 1 and the first k that statisfy with the condition is the minimum
        # start from k = 1 and calculate the time h' to finish every piles of banana
        # if h' larger than h move to next k
        # find the first k' such that its h' == h or h' > h
        # TC: O(max(piles) * piles.length)
            # worst case is that there is a huge pile and k has to be the max pile to find the answer. Also, for 
            # each k we have to iterate through pile list to calculate h

        # binary search approach:
        # from brute force we know that the range of the k would be 1 to max(p)
        # we want to optimize the k searching method by applying binary search on k list
        # assign left pointer to start of k and right pointer to end of k
        # calculate the mid point as use it as k'
        # calculate the h' with the k' (mid pointer)
            # if h' > h shift l to mid + 1 (at the k' eating speed, koko cannot finish in time)
            # if h' <= h shift r to mid - 1 (at the k' eating speed, koko can finish in time)
                # record the answer 


        l, r = 1, max(piles) # since k is an array from [1...max(piles)] we do not need to create a list for that
        k = 0

        while l <= r:
            mid = (l + r) // 2     
            
            currH = 0 
            for p in piles:
                currH += ceil(p/mid)

            if currH > h:
                l = mid + 1
            elif currH <= h:
                k = mid
                r = mid - 1
        
        return k

        # TC: O(log(max(piles)) * piles.length)
        # SC: O(1)


if __name__ == "__main__":

    s = Solution()

    r1 = s.minEatingSpeed(piles = [3,6,7,11], h = 8)
    r2 = s.minEatingSpeed(piles = [30,11,23,4,20], h = 5)

    print(r1)
    print(r2)

