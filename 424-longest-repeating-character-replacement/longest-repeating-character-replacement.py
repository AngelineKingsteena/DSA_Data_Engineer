class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## video solution :- https://www.youtube.com/watch?v=gqXU1UyA8pk&ab_channel=NeetCode
        ### IDEA: we need to get longest repeating string,
        # so the logic we'll be using is :- length of sring sofar-max count of char/Count of repeating char sofar> k 
        # (r - l + 1) - maxf <= k
        # if not so move the left ,move left pointer
        count = {}
        res= 0
        l = 0
        maxf = 0
        for r in range(len (s)):
            count [s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                # we want to move left pointer ahead,so count of char at l,should be considered for reduction
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        