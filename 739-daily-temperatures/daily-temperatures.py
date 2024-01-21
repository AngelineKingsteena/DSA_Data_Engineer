class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## video solution :-https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode
        ## only store next heighest temp ...implicitly means to pop lesser temp
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        for i, t in enumerate (temperatures):
            while stack and t > stack[-1][0]:#once you meet next highest
                stackT, stackInd = stack. pop() ## keep popping until u get to end of stack/in res[] index of previous highest
                # update res at popped index with value of diff bet. current max temp's index and popped index
                res [stackInd] = (i - stackInd)
            ## after above cal,then add cuurent max tmp & index
            stack.append([t, i]) ## keep adding without popping until u get next highest
        return res
        
