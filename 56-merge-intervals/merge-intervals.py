class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # https://www.youtube.com/watch?v=44H3cEC2fFM&ab_channel=NeetCode
        # O(nlogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals [0]]
        for start, end in intervals[1:]:
            lastEnd = output [-1][1]
            if start <= lastEnd:
                output [-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
        