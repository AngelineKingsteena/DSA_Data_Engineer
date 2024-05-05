class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # SLIDE LEFT (EXPLANATION 10 MIN IN VIDEO)
        #T.C :- O(n)
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
            # (r - l + 1) = length of string but also considered here as window
            # maxf here indicates maximum letter here in this window
            # example :- lallllla ,if window is 6-0+1,maxf of 'l' is 6,
            # this way we ensure we get largest string with minimal i.e k replacements only
            while (r - l + 1) - maxf > k:
                # we want to move left pointer ahead,so count of char at l,should be considered for reduction
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
