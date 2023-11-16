class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## video solution :-https://www.youtube.com/watch?v=wiGpQwVHdE0&ab_channel=NeetCode
        charSet = set()
        l = 0
        res = 0
        for r in range(len (s)):
            ## keep moving left pointer and removing prior occurances of said characters identified by left pointer
            while s[r] in charSet:
                charSet.remove(s [l]) ## note s[l] and not s[r]-->s[l] points to prior occurances of said character
                l += 1
            ## post duplicate handling by left pointer,progress through with right pointer
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        
