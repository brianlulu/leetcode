class Solution:
    def insert(self, intervals, newInterval):
        
        # input: intervals -> List[List[int]]; newInterval -> List[int]
        # output: intervals after insertion and merge -> List[List[int]]
        result = []
        # iterate through intervals
        for cur in intervals:
            # non overlap
            if cur[0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[intervals.index(cur):]
            elif cur[1] < newInterval[0]:
                result.append(cur)
            #overlap
            else:
                newInterval = [min(cur[0], newInterval[0]), max(cur[1], newInterval[1])] 
        
        # for case that all intervals merge to one or there is empty interval
        result.append(newInterval)

        return result

    
    '''
    Time Complexity: O(N) iterate through list once
    Space Complexity: O(N) the result list store n intervals
    '''

if __name__ == "__main__":

    s = Solution()

    r1 = s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
    r2 = s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])

    print(r1)
    print(r2)
                