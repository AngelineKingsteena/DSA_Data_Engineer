class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # https://www.youtube.com/watch?v=EgI5nU9etnU&ab_channel=NeetCode
        # map each course to prereq list
        preMap = { i: [] for i in range (numCourses) }
        for crs, pre in prerequisites:
            preMap [crs].append (pre)
        
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs) :
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses) :
            if not dfs(crs): return False
        return True
        # 1 -> 2
        # 3 -> 4
                