class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # https://www.youtube.com/watch?v=9z2BunfoZ5Y&ab_channel=NeetCode

        # T.C :- O(m*n)
        ## IDEA:- follow the phase comments

        ROWS, COLS = len (board), len (board[0])
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
            or board[r][c] != "O"):
                return
            board[r][c] = "T"
            ### in [["O","O","O"],["O","0","O"],["O","O","O"]],
            ## to make O->T in the center,also
            capture(r + 1, c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r, c-1)
        #phase 1. (DFS) mark unsurrounded regions with temperory T(0 -> T)
        for r in range(ROWS) :
            for c in range(COLS) :
                if (board[r][c] == "O" and
        (r in [0, ROWS - 1] or c in [0, COLS - 1])):
        #  (r in [0, ROWS - 1] or c in [0, COLS - 1])) == BORDER REGIONS
                    capture(r, c)
        #phase 2. Capture surrounded regions (0 -> X)
        for r in range(ROWS) :
            for c in range (COLS) :
                if board[r][c] == "O":
                    board[r][c] = "X"
        #phase 3. Revert the T (T -> 0)
        for r in range (ROWS) :
            for c in range (COLS):
                if board[r][c] == "T":
                    board[r][c] ="O"
                