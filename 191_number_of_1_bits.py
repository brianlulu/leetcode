class Solution:
    def hammingWeight(self, n):
        res = 0

        while n > 0:
            res += n % 2
            n >>= 1
        
        return res


if __name__ == "__main__":

    s = Solution()
    r1 = s.hammingWeight(11)

    print(r1)