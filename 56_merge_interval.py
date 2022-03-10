class Solution:
    def merge(self, intervals): 
        intervals.sort(key = lambda interval : interval[0])
        
        result = [intervals[0]]
        #iteration
        for start, end in intervals[1:]:
            # check next element overlap
            pre_interval = result[-1]
            if start <= pre_interval[1]:
                result[-1] = [min(start, pre_interval[0]), max(end, pre_interval[1])]
            # or not 
            else:
                result.append([start, end])
        
        return result

    '''
    Time Complexity: O(N) check overlap O(NlogN) is the sort
    Space Complexity: O(N)
    '''
    
    '''
    intervals = [[1,4],[4,5]]
    result = [[1,4]]
    pre_interval = [1,4]  result = [[1,5]], start = 4, end = 5
    
    [[1,3],[2,6],[8,10],[15,18]]
    result = [[1,3]]
    
    pre_interval = [1,3]  result = [[1,3]], start = 2, end = 6
    '''