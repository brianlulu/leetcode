class Solution:
    def dailyTemperatures(self, temperatures):
        
        # input: temperatures -> List[int]
        # output: how many days after to have a warmer temp -> List[int]

        # constraints:
        # temperatures.length >= 1
        # temperatures[i] >= 30
        # warmer means temperature[i] > temperature[j]

        # brute force approach:
        # iterate through each day
        # at each index/day find the future day that is warmer
        # TC: O(N^2)
        # SC: O(1)

        # monotonic decreasing stack (not strict decreasing)
        # iterate through the temperature array
        # use a stack to keep track the unsolved index,
        # meaning we havent find any future warmer day for the current index
        # if the current iteration has a warmer temp than the top of the stack
        # we can record the answer and pop the top element of the stack
        # if not, just push into the stack and look for future days

        stack = []
        result = [0] * len(temperatures) # the default is that we cannot find any possible future days

        for i in range(len(temperatures)):
            curr = temperatures[i]
            
            while stack and stack[-1][0] < curr:
                pastTemp = stack.pop()
                result[pastTemp[1]] = i-pastTemp[1]

            stack.append((curr, i))
        
        return result

        # TC: O(N)
        # SC: O(N)


if __name__ == "__main__":

    s = Solution()
    r1 = s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
    r2 = s.dailyTemperatures(temperatures = [30,40,50,60])

    print(r1)
    print(r2)