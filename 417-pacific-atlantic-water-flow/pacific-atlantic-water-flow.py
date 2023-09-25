class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # https://www.youtube.com/watch?v=s-VkcjHqkGI&ab_channel=NeetCode
        # T.C : O(m*n)
        # idea:- start from extremeties like top row and left column for pacific
        # and bottom row and right column for atlantic and keep marking these cell in visited
        # set i.e pac and atl...if the same cell is in both pac and atl return it as result

        ROWS, COLS = len (heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
            r < 0 or c < 0 or r == ROWS or c == COLS or
            heights [r][c] < prevHeight):
            #heights [r][c] < prevHeight coz we are moving from out to in,
            # our need is heights [r][c] > prevHeight
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS) :
            dfs(0, c, pac, heights [0][c])
            dfs (ROWS - 1, c, atl, heights [ROWS - 1][c])

        for r in range(ROWS) :
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][c])

        res = []
        for r in range (ROWS) :
            for c in range (COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
        return res