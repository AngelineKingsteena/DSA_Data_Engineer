from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()  # (r, c) tuples to keep track of visited cells
        memo = {}  # Memoization dictionary

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or
                    c < 0 or c == COLS or
                    matrix[r][c] <= prevVal or
                    (r, c) in visited):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            visited.add((r, c))

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            visited.remove((r, c))
            memo[(r, c)] = res

            return res

        max_lip = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_lip = max(max_lip, dfs(r, c, -1))

        return max_lip
