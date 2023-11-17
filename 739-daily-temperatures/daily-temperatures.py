class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## video solution :-https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate (temperatures):
            while stack and t > stack[-1][0]:#once you meet next highest
                stackT, stackInd = stack. pop() ## keep popping until u get to end of stack/in res[] index of previous highest
                res [stackInd] = (i - stackInd)
            stack.append([t, i]) ## keep adding without popping until u get next highest
        return res
        
