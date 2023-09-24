class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # The problem can be solved with DFS. Time complexity: O(height * width), space complexity: O(height * width).
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # DFS
        if len(grid) == 0:
            return 0
        count = 0
        visit = set()
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and (i,j) not in visit:
                    count += 1
                    stack = [(i,j)]
                    while stack:
                        u = stack.pop()
                        visit.add(u)
                        h, w = u[0], u[1]
                        if h > 0 and grid[h-1][w] == '1' and (h-1,w) not in visit:
                            stack.append((h-1,w))
                        if h < height - 1 and grid[h+1][w] == '1' and (h+1,w) not in visit:
                            stack.append((h+1,w))
                        if w > 0 and grid[h][w-1] == '1' and (h,w-1) not in visit:
                            stack.append((h,w-1))
                        if w < width - 1 and grid[h][w+1] == '1' and (h,w+1) not in visit:
                            stack.append((h,w+1))
        return count

