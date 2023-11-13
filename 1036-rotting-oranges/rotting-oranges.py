class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # https://docs.google.com/document/d/1l9UDlLZeP0mQxExqjepsKbgYQj4nrNGUsyDlKDA1jyg/edit
        m, n, time = len(grid), len(grid[0]), 0
        rotten, fresh = deque(), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: fresh.add((i,j))
                if grid[i][j] == 2: rotten.append((i,j,0))
        ## rotten being a queue,will have the order of 1st rotten
        while rotten:
            x, y, step = rotten.popleft()
            time = step
            # i=x+1,x-1,x,x
            for i, j in ((x+1, y), (x-1, y), (x, y+1),(x, y-1)):
                #If an adjacent cell contains a fresh orange
                if (i, j) in fresh:
                    #add it to the rotten queue, and
                    #  record the step (minute) at which it rots.
                    rotten.append((i, j, step+1))
                    fresh.remove((i, j))
        return -1 if fresh else time

        
