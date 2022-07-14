from unicodedata import name


class Solution:
    def trap(self, height):

        # input: height -> List[int]
        # output: area that the water can be trapped by the map

        # Contraints:
        # height.length >= 1
        # height[i] >= 0

        # Two pointer approach:
        # For an valid terrain to trap water, the bottleneck will be min (max left neighbors, max right neighbors)
        """
        Graphic example
                #
        #       #
        #   #   #
        1   2   3

        current water trap = min(maxL, maxR) - height[i]
        at index 1, maxL = 0 maxR = 3, 0 - 2 = -2 => 0
        at index 2, maxL = 2 maxR = 3, 2 - 1 = 1 
        at index 3, maxL = 2 maxR = 0, 0 - 3 = -3 => 0

        by the nature of this problem, we need the maxL maxR. We can use two pointer approach to keep track that!
        """
        
        l, r = 0 , len(height)-1
        result = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL > maxR:
               r -= 1
               maxR = max(height[r], maxR)
               currWater = min(maxR,maxL) - height[r]
               if currWater > 0:
                result += currWater
            else:
                l += 1
                maxL = max(height[l], maxL)
                currWater = min(maxR,maxL) - height[l]
                if currWater > 0:
                    result += currWater
        
        return result

if __name__ == "__main__":

    s = Solution()

    r1 = s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
    r2 = s.trap(height = [4,2,0,3,2,5])

    print(r1)
    print(r2)


     
