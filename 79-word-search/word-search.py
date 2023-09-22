class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ## video solution :- https://www.youtube.com/watch?v=pfiQ_PS1g8E&ab_channel=NeetCode

        ## idea:-
        # start looking for the starting letter of word in board,
        # until then dfs,keeps returning false.
        # if starting letter of word is found in board,then look in
        # all four directions of it,concurrently updating i
        # if if next letter is not found in the 4 directions,
        # pop out the starting letter,maybe its the duplicate and has
        # nothing to do with word

        ROWS, COLS = len (board), len(board[0])
        path = set ()
        def dfs(r, c, i):
            if i == len (word):
                return True
            if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or
            (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i +1) or
            dfs(r - 1,c,i+1) or
            dfs(r, c + 1,i+1) or
            dfs(r, c - 1,i+1))
            path.remove((r, c))
            return res
        for r in range(ROWS) :
            for c in range (COLS):
                if dfs(r, c, 0): return True
        return False
        # 0(n * m * 4^n)
                