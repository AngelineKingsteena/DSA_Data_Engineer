class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## video solution :-https://www.youtube.com/watch?v=wiGpQwVHdE0&ab_channel=NeetCode
        charSet = set()
        l = 0
        res = 0
        for r in range(len (s)):
            ## we're not looking for subset,rather substring,so "baabc",at iteration r=2,l will remove 0th b & 1th a,
            ## so charset will become empty in while loop
            ## outside while loop charset would get s[2]=a
            while s[r] in charSet:
                charSet.remove(s [l]) ## note s[l] and not s[r]-->s[l] points to prior occurances of said character
                l += 1
            ## post  handling substrings which had duplicate element 
            ## (eg: in "'acd'd",acd will be removed by while coz last d is a duplicate occurence ) 
            ## by left pointer,progress through with right pointer
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        
