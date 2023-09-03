class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
         store the indexs of the numbers in a dictionary in (x, y) format. Then for every number check for same row, same col and same box condition.
This will require a single traversal. The same box condition can be checked using pos[0]//3 == x//3 and pos[1]//3 == y//3 since i//3 and j//3 give the box position.
        """
        boardMap = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.': 
                    if char in boardMap:
                        for pos in boardMap[char]:
                            # check if its in same x-axis or y-axis or
                            # (comes within the 3*3 box)
                            # pos is old position of char,(x,y) will become
                            # new position of char if they pass below
                            # condition
                            if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    boardMap[char].append((x,y))
   
        return True