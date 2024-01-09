class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # https://www.youtube.com/watch?v=EgI5nU9etnU&ab_channel=NeetCode
        # map each course to prereq list
        ## eg:-numCourses=2,prerequisites=[[1,0],[0,1]]
        ## preMap = {0: [1], 1: [0]}
        preMap = { i: [] for i in range (numCourses) }
        
        for crs, pre in prerequisites:
            preMap [crs].append (pre)
        
        # visitSet = all courses along the curr DFS path
        cycle = set()
        def dfs(crs) :
            if crs in cycle:
                return False
            if preMap[crs] == []:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
                else:
                    continue
            cycle.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses) :
            if not dfs(crs): 
                return False
            else:
                continue
        return True
        # 1 -> 2
        # 3 -> 4
                
