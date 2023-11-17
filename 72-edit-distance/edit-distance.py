class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
# https://www.youtube.com/watch?v=XYi2-LPrwm4&ab_channel=NeetCode
        ## no.rows=len(word1) + 1
        ## no.columns=len(word2) + 1
        #          w2
        #       a c d ""
        # w1  a       3
        #     b       2
        #     d   1 0 1
        #     " 3 2 1 0
        cache = [[float("inf")] * (len (word2) + 1) for i in range(len(word1) + 1)]
        for j in range(len (word2) + 1):
            cache[len (word1)][j] = len(word2) -j
        for i in range(len (word1) + 1):
            cache [i][len (word2)] = len(word1)-i
        for i in range(len (word1) - 1,-1,-1):
            for j in range(len (word2)- 1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    ### 1+ COZ 1 EDIT
                    cache [i][j] = 1 +min(cache[i + 1][j], cache[i][j + 1], cache [i+1] [j+1])
        return cache[0][0]        
