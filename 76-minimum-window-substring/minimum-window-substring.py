class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## video solution :-https://www.youtube.com/watch?v=CX6_L9GLldU&ab_channel=TimothyHChang

        """
        Intuition:

We maintain two pointers, start and end, to represent a window in the string s.
Initially, we move the end pointer to the right, expanding the window, until we include all the characters from string t in the window.
Then, we move the start pointer to the right, shrinking the window while still maintaining the requirement of having all characters from t. This helps us find the minimum window size that satisfies the condition.
We keep track of the minimum window size and its corresponding substring as we iterate through the entire string s.
        """
        lookup = Counter(t)
        miN = float("inf")
        output = ""
        S=len(s)
        start,end = 0,0
        count = len(lookup)
        #ADOBECODEBANC
        
        while end < S:
            #end pointer
            while end < S and count!=0:
                if s[end] in lookup:
                    lookup[s[end]] -= 1
                    if lookup[s[end]] == 0:
                        count -= 1
                end+=1
            #start pointer
            while start<end and count == 0:
                if end-start < miN:
                    miN = end-start
                    output = s[start:end]
                if s[start] in lookup:
                    lookup[s[start]] += 1
                    ## in "ADOBECODEBANC" if we need 1 count 
                    ## of b and have 2 b's ,then
                    ## lookup[s[start]]+=1 would have made -1 as 0, so as long 
                    ## as we have enough just enough b's in o/p
                    ## string (i.e lookup[s[start]]>0) then do
                    ## count += 1,to move "end" to search in closer 
                    ## vicinity of this extra b
                    if lookup[s[start]]>0:
                        count += 1
                start+=1
            
        return output
        