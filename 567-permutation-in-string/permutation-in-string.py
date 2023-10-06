class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## video solution :-https://www.youtube.com/watch?v=VIR699JK4Yg&ab_channel=PersistentProgrammer
        lookup1 = [ord(i) - ord('a') for i in s1]
        lookup2 = [ord(i) - ord('a') for i in s2]
        # lookup1 = [0, 1] ab
        # lookup2 = [4, 8, 3, 1, 0, 14, 14, 14] eidbaooo
        ## target and window will use values of lookup1 &2 as indices,
        ## and their values will be count of char
        target = [0] * 26
        window = [0] * 26
        for freq in lookup1:
            target[freq]+=1
        # target = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        for i, freq in enumerate(lookup2):#[4, 8, 3, 1, 0, 14, 14, 14]
            window[freq] += 1
            ## to indicate already looked at [4,8] time to look at [8,3]
            ## in [4, 8, 3, 1, 0, 14, 14, 14] eidbaooo ,for s1="ab"
            if i >= len(s1): #window size exceeded
                rem = i - len(s1) # at index 2,index 0 is out of window
                window[lookup2[rem]] -= 1 
            if window == target:
                return True
        return False
                