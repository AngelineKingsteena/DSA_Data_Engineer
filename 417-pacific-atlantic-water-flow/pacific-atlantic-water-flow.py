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
            ###keep visiting nearby valid cells,from the current valid cell
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS) :
            #top row for pacific and bottom row for atlantic
            dfs(0, c, pac,-1)
            dfs (ROWS - 1, c, atl, -1)

        for r in range(ROWS) :
            # left column for pacific & right column for atlantic
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)
        
        return pac & atl ##present in both