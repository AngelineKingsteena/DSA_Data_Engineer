class Solution:
    # https://www.youtube.com/watch?v=3Rw3p9LrgvE&ab_channel=NeetCode
    ## in video from 10 min mark
    ##memoisation
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
                ## dfs(i+1 coz we just used i for comparison,look in bottom
            ### why  s1[i] == s3[i+j] ,explanation in 4:30 min & dfs(i+1 coz we just used i in s1[i] == s3[i+j]
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j): #s3[i+j] coz say i=2,j=2, we expect s3 4th index value to match
                return True
                ## dfs(i+1 coz we just used i for comparison,look in right
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            return False
        return dfs(0,0)
        
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #     dp = [ [False]*(len(s2) + 1) for i in range(len (s1) + 1)]
    #     dp[len (s1)][len (s2)] = True
    #     for i in range(len (s1), -1, -1):
    #         for j in range (len (s2), -1,-1):
    #             ##11:25 timestamp on video
    #             ## look in the bottom
    #             if i<len(s1) and s1[i] == s3[i+j] and dp[i + 1][j]:
    #                 dp[i][j] = True
    #             ## look in the right
    #             if j<len(s2) and s2[j] == s3[i+j] and dp[i][j + 1]:
    #                 dp[i][j] = True
    #     return dp[0][0]
