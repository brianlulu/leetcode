class Solution:
    def eraseOverlapIntervals(self, intervals):
        
        # input: intervals -> List[List[int]]
        # output: # of minimum removal -> int

        # Python sort by first element by default
        intervals.sort() 
        
        result = 0
        pre_end = intervals[0][1]
        
        # iterate through intervals
        for start, end in intervals[1:]:
            # if overlap
            if pre_end > start:
                result += 1
                pre_end = min(end, pre_end)
            # if non-overlap
            else:
                pre_end = end
            
        return result
    
    
    '''
    Time Complexity: O(nlogn) sort algorithm
    Space Complexity: O(N) for sort otherwise O(1)
    
    intervals = [[1,2],[1,3], [2,3],[3,4]] 
    
    result = 0, pre_end = 2
    
    start = 1, end = 3, pre_end = 2, result = 1
    start = 2, end = 3, pre_end = 3, result = 1
    start = 3, end = 4, pre_end = 3, result = 1
    
    '''