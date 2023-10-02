class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # https://www.youtube.com/watch?v=Ua0GhsJSlWM&ab_channel=NeetCode

        ##idea:-
        # create a 2 d matrix of text1 & text2 with extra row and extra column and if the letters match,then add 1 with diigonal value,else move  right or botom and take max of either

        ## logic
    #         a  b  ""
    #       ----------
    #     a |  |  | 0
    #     c |  |  | 0
    #     b |  |1 | 0 ## here 0,coz if we match "" with "",0 lcs; 1 coz if match "b" with "b"
    #    " "|0 | 0| 0

    ## max(right,bottom) when mismatch,coz in below,if u go down lcs=2,but on right lcs=1
        # c  e  ""
#       ----------
#     c |  |  | 0
#     d |  |  | 0
#     e |  |1 | 0 
#    " "|0 | 0| 0

# range(len(text2) + 1) becoz that extra 0
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