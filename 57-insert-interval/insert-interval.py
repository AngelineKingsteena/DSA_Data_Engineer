class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
# https://www.youtube.com/watch?v=A8NUOmlwOlM&ab_channel=NeetCode
        res = []
        for i in range(len (intervals)):
            ## new intervals end< current ith interval's start
            ## then add new interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            ## new intervals start> current ith interval's end
            ## then add ith interval
            elif newInterval[0] > intervals[i][1]:
                res.append (intervals[i])
            else:
                ##if new interval is overlapping,loop thru all 
                # ith inteval,and take extremeties from 
                # all i intevals and create custom new interval,
                ##BUT DONT ADD IT YET,CAUSE KEEP LOOPING 
                # UNTIL ALL iTH INTERVAL'S ENDS FALL UNDER
                # NEW INTERVAL'S END
                newInterval = [min(newInterval[0], intervals [i][0]), max(newInterval [1], intervals [i][1])]
        res.append (newInterval)
        return res
        