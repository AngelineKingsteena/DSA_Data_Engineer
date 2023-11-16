class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # bottom left is asseced as matrix[bottom - i][l],whereas top left as matrix[top][l + i] because desired direction is anticlockwise
        # a→...b
        # .    ↓
        # .    .
        # ↑    .  as u can see value in bottom left  will keep
        # d...←c  moving upward,hence matrix[bottom - i][l]
        l, r = 0, len(matrix) - 1
        top, bot = l, r
        while l < r:
            for i in range(r-l):
                # save the topleft
                topleft = matrix[top][l + i]
                # move bottom left into top left
                matrix[top][l + i] = matrix[bot - i][l]
                # move botton right into bottom left
                matrix[bot - i][l] = matrix[bot][r - i]
                # move top right into botton right
                matrix[bot][r - i] = matrix[top + i][r]
                # move top left into top right
                matrix[top + i][r] = topleft
            r -= 1
            l += 1
            top += 1
            bot -= 1

                
