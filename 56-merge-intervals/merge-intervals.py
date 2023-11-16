class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # https://www.youtube.com/watch?v=44H3cEC2fFM&ab_channel=NeetCode
        # O(nlogn)
        ## sort by start time
        intervals.sort(key = lambda i : i[0])
        output = [intervals [0]]
        for start, end in intervals[1:]:
            latestEnd = output [-1][1]
            ## if next interval starts before/on time with prev interval's end
            ##  prev  --------             -------
            ##  curr      ----------   or         -----
            if start <= latestEnd:
                output [-1][1] = max(latestEnd, end)
            else:
            ##  prev  --------- 
            ##  curr                  -----
                output.append([start, end])
        return output
        
