class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # https://www.youtube.com/watch?v=Ua0GhsJSlWM&ab_channel=NeetCode
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len (text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    ## diagonal
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    ## max(right,bottom)
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]