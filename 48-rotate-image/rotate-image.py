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
        while l < r:
            for i in range(r - l):
                top, bottom = l,r
                # save the topleft
                topLeft = matrix[top][l + i]
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move botton right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right into botton right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left into top right
                matrix[top + i][r] = topLeft
            r-=1
            l+=1
                