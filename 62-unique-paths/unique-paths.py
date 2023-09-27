class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # https://www.youtube.com/watch?v=IlEsdxuD4lY&ab_channel=NeetCode

# idea:- replicate below (notice last row ,last column is fully 1)
        # 28,21,15,10,6,3,1
        #  7, 6, 5, 4,3,2,1 (2=right+down ,3=right+down)
        #  1, 1, 1, 1,1,1,1
        # start location is 1,end is 28

        #act as last row with n columns
        row = [1] * n
        # all rows except last one
        for i in range(m - 1):
            #after 1st full iteration #  1, 1, 1, 1,1,1,1
            #after 2nd full iteration #  7, 6, 5, 4,3,2,1
            newRow = [1] * n
            #to do right,leave last column that's why n-2
            for j in range(n - 2, -1, -1):
                #after 1st full iteration #  7, 6, 5, 4,3,2,1
                #after 2nd full iteration # 28,21,15,10,6,3,1
                #newRow[j + 1]=right ,row[j]=down
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
        