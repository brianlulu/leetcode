class Solution:
    def maxArea(self, height):

        # input = height [int]
        # output = int
        res = 0
        l , r = 0, len(height) - 1

        while l < r:

            curArea = (r - l) * min(height[l], height[r])
            res = max(res, curArea)

            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return res


if __name__ == "__main__":

    s = Solution()

    r1 = s.maxArea([1,8,6,2,5,10,8,3,7])
    r2 = s.maxArea([1,1])
    r3 = s.maxArea([1,2,3,4,5,6,7])

    print(r1, r2, r3)