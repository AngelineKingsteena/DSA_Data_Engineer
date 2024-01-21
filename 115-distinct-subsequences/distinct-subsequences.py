class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # Create a 2D DP matrix to store intermediate results
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the matrix with base cases
        ## places where t is empty
        for i in range(m + 1):
            ## all rows of column n--> t is over and now nth column is "" char
            dp[i][n] = 1

        # Iterate through the matrix to fill in the values
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]

# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
# # https://www.youtube.com/watch?v=-RDzMJ33nx8&ab_channel=NeetCode
# ##i=index of s, j=index of t
#         cache = {}
#         def dp(i, j):
#             if j == len(t):
#                 return 1
#             if i == len(s):
#                 return 0
#             if (i, j) in cache:
#                 return cache[(i, j)]
#             if s[i] == t[j]:
#                 #s="bby" t="by" 
#                 #dfs(i + 1, j + 1) ,means maybe 0th index b in s matches with t'b,
#                 #so we can  check move on to check next characters in s(i+1) and t(j+1)
#                 #dfs(i + 1, j) ,means maybe 1th(next) index b in s(i+1) matches with t'b(j) 
#                 #without shifting character in t

#                 # the + b/w dfs is like "maybe" this or that
#                 #SIMPLE
#                 #dfs(i + 1, j + 1) = CURRENT I&J MATCHED MOVE TO NEXT characters in both s&t
#                 #dfs(i + 1,j) = CURRENT I&J MATCHED MOVE TO NEXT character just in s, 
#                 #cause s may(no guarantee it'll match,if it doesn't match 0 will be returned)
#                 #have duplicate characters 
#                 cache[(i, j)] = dp(i + 1, j + 1) + dp(i + 1, j)
#             else:
#                 #didnt match,so maybe next character of s may match current character of t
#                 cache [(i, j)] = dp(i + 1, j)
#             return cache[(i, j)]
#         return dp(0, 0)
        
