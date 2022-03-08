class Solution:
    def canFinish(self, numCourses, prerequisites):

        # input: numCourse -> int, prerequisties -> [[int]]
        # output: whether the course can be taken -> Boolean

        # prereq Hash Map
        prereqHM = { i:[] for i in range(numCourses)}
        
        for crs, prereq in prerequisites:
            prereqHM[crs].append(prereq)
    
        # visitedCourse
        visitedCrs = set()

        # DFS approach
        def dfs(crs):
            # if current course in visitedCourse; return False
            if crs in visitedCrs:
                return False
            # if current course's prereq hash map is []; return True
            if prereqHM[crs] == []:
                return True 

            visitedCrs.add(crs)
            for pre in prereqHM[crs]:
                if not dfs(pre):
                    return False  

            # Optimized for visit repeat course
            visitedCrs.remove(crs)    
            prereqHM[crs] = []

            return True

        # we need to do this for the case of two separate graph
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

if __name__=="__main__":

    s = Solution()
    r1 = s.canFinish(5, [[0,1],[0,2],[1,3],[1,4],[3,4]])

    print(r1)