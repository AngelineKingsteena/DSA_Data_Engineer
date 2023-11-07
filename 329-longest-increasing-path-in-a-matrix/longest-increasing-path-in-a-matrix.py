class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=wCc_nd-GiEc&ab_channel=NeetCode
        ROWS, COLS = len (matrix), len(matrix[0])
        dp = {} # (r, c)-->LIP
        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or
            c < 0 or c == COLS or
            matrix[r][c] <= prevVal):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            """
            max becoz in input
            9,9,4
            6,6,8
            2,1,1
            the dfs lip matrix looks like below, wherein each element 
            indicates lip from itself that's 1+x
            1,1,2
            2,2,1
            3,4,2
            the last middle one in i/p can go up or right
            max(up (1+2), right(1+3))
            """
            res = 1
            res = max(res, 1 + dfs(r+1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r-1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1,matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1,matrix[r][c]))
            dp[(r, c)] = res
            return res
        for r in range(ROWS) :
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp. values ())
                
