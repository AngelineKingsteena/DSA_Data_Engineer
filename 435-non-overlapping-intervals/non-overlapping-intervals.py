class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # https://www.youtube.com/watch?v=nONCGxWoUfM&ab_channel=NeetCode
        intervals.sort()
        prevend=intervals[0][1]
        count=0
        for start,end in intervals[1:]:
             ## if next interval starts before with prev interval's end
            ##  prev  --------        
            ##  curr      ----------   
            if start<prevend:
                count+=1
                prevend=min(prevend,end)
            else:
            ##  prev  --------        or           ------
            ##  curr  --------                --------
                prevend=end
        return count
