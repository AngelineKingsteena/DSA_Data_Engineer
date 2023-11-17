class Solution:
# in example 2
#     The code starts by iterating through the grid and encounters the first '1' at (0, 0).
# It initiates a DFS traversal from (0, 0) and explores all connected land cells, marking them as visited and adding them to the stack.
# The traversal covers the first island.
# It increments the count to 1.
# The code then continues to iterate through the grid and encounters another '1' at (2, 2).
# It initiates a DFS traversal from (2, 2) and explores all connected land cells, marking them as visited and adding them to the stack.
# The traversal covers the second island.
# It increments the count to 2.
    def numIslands(self, grid: List[List[str]]) -> int:
        # The problem can be solved with DFS. Time complexity: O(height * width), space complexity: O(height * width).
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROW, COL = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROW or c == COL or grid[r][c] != "1" or (r, c) in visit:
                return
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i, j) not in visit: ## crucial to check not in visit,cause this (i,j) is 
                    # already part of another island,so no need to reconsider
                    islands += 1
                    dfs(i, j)
        return islands

